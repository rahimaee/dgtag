from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from django.urls import reverse

from mytag_cards.models import Card
from mytag_cards_map.models import Map
from userpanel_map.forms import MapForm
from django import forms


@login_required(login_url='/login')
def all_map_user(request):
    all_map = Map.objects.filter(By_User=request.user).all()
    context = {
        'all_map': all_map
    }
    return render(request, 'userpanel_map/all_map_user.html', context)


@login_required(login_url='/login')
def add_map_user(request):
    all_user_card = Card.objects.filter(created_by=request.user.id)
    my_card_tuple = ((n.pk, n.get_name()) for n in all_user_card)
    Map_Form = MapForm(request.POST or None, request.FILES)

    Map_Form.fields['DgTag'].widget = forms.Select(choices=my_card_tuple)

    if Map_Form.is_valid():
        add_map = Map()
        add_map.By_User = request.user
        add_map.Country = Map_Form.data.get('Country')
        add_map.Province = Map_Form.data.get('Province')
        add_map.City = Map_Form.data.get('City')
        add_map.Name = Map_Form.data.get('Name')
        add_map.DgTag = Card.objects.filter(pk=Map_Form.data.get('DgTag')).first()
        add_map.Address = Map_Form.data.get('Address')
        add_map.Lat = Map_Form.data.get('Lat')
        add_map.Lng = Map_Form.data.get('Lng')
        add_map.MapImg = Map_Form.data.get('MapImg')
        MapImg = Map_Form.cleaned_data.get('MapImg')
        add_map.MapImg = MapImg
        add_map.MapText = Map_Form.data.get('MapText')
        add_map.save()

    context = {
        'Map_Form': Map_Form
    }
    return render(request, 'userpanel_map/add_map_user.html', context)


@login_required(login_url='/login')
def view_map_user(request, *args, **kwargs):
    context = {}
    if request.method == "GET":
        map_id = kwargs.get('MapId')
        map = Map.objects.filter(pk=map_id, By_User=request.user).first()
        context['map'] = map

    return render(request, 'userpanel_map/view_map_user.html', context)


@login_required(login_url='/login')
def update_map_user(request, *args, **kwargs):
    context = {}
    map_id = kwargs.get('MapId')
    user_map = Map.objects.filter(pk=map_id).first()
    if request.method == "GET":
        Map_Form = MapForm(request.POST or None, initial={
            'Name': user_map.Name,
            'Country': user_map.Country,
            'Province': user_map.Province,
            'City': user_map.City,
            'Address': user_map.Address,
            'Lat': user_map.Lat,
            'Lng': user_map.Lng,
            'MapImg': user_map.MapImg,
            'MapText': user_map.MapText,
            'DgTag': user_map.DgTag_id,

        })
        all_user_card = Card.objects.filter(created_by=request.user.id)
        my_card_tuple = ((n.pk, n.get_name()) for n in all_user_card)
        Map_Form.fields['DgTag'].widget = forms.Select(choices=my_card_tuple)
        context['Map_Form'] = Map_Form

    if request.method == "POST":
        Map_Form = MapForm(request.POST or None, request.FILES, initial={
            'Name': user_map.Name,
            'Country': user_map.Country,
            'Province': user_map.Province,
            'City': user_map.City,
            'Address': user_map.Address,
            'Lat': user_map.Lat,
            'Lng': user_map.Lng,
            'MapImg': user_map.MapImg,
            'MapText': user_map.MapText,
            'DgTag': user_map.DgTag_id,
        })
        if Map_Form.is_valid():
            all_user_card = Card.objects.filter(created_by=request.user.id)
            my_card_tuple = ((n.pk, n.get_name()) for n in all_user_card)
            Map_Form.fields['DgTag'].widget = forms.Select(choices=my_card_tuple)
            Name = Map_Form.cleaned_data.get('Name')
            Country = Map_Form.cleaned_data.get('Country')
            Province = Map_Form.cleaned_data.get('Province')
            City = Map_Form.cleaned_data.get('City')
            Address = Map_Form.cleaned_data.get('Address')
            Lat = Map_Form.cleaned_data.get('Lat')
            Lng = Map_Form.cleaned_data.get('Lng')
            MapImg = Map_Form.cleaned_data.get('MapImg')
            MapText = Map_Form.cleaned_data.get('MapText')
            user_map.Name = Name
            user_map.Country = Country
            user_map.Province = Province
            user_map.Address = Address
            user_map.City = City
            user_map.Lat = Lat
            user_map.Lng = Lng
            user_map.MapImg = MapImg
            user_map.MapText = MapText
            user_map.DgTag = Card.objects.filter(pk=Map_Form.data.get('DgTag')).first()
            user_map.save()
            return redirect(reverse('userpanel_map:detail_map', args=[user_map.pk]))

    return render(request, 'userpanel_map/update_map_user.html', context)
