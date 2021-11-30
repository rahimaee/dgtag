from django.http import Http404
from django.shortcuts import render, redirect, reverse
from mytag_cards.models import Card
from mytag_cards_contactnumbers.models import ContactNumbers


# Create your views here.

def checkInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


# business cards page
def my_tag_home(request, *args, **kwargs):
    card = kwargs.get('card')
    mytag = ''
    context = {}
    if card is not None:
        if checkInt(card) is True:
            mytag = Card.objects.card_by_card_id(card)
            if mytag is None:
                raise Http404()
            if mytag.UserName is not None and mytag.IsActiveUserName is True:
                return redirect(reverse('cards:my_tag_home', kwargs={'card': mytag.UserName}))
            if mytag.TypeOfCard_id == 1:
                mytag.Views += 1
                mytag.save()
                contact_numbers = mytag.has_ContactNumbers.filter(IsActive=True).all()
                socialnetworks = mytag.socialnetwork_set.filter(IsActive=True).all()
                context['numbers'] = contact_numbers
                context['socialnetworks'] = socialnetworks
                context['mytag'] = mytag
                return render(request, 'mytag_cards/business_tag_home.html', context)
            else:
                raise Http404()
        elif isinstance(card, str):
            mytag = Card.objects.card_by_user_name(card)
            if mytag is None:
                raise Http404()
            if mytag.TypeOfCard_id == 1:
                mytag.Views += 1
                mytag.save()
                contact_numbers = mytag.has_ContactNumbers.filter(IsActive=True).all()
                socialnetworks = mytag.socialnetwork_set.filter(IsActive=True).all()
                context['numbers'] = contact_numbers
                context['socialnetworks'] = socialnetworks
                context['mytag'] = mytag
                return render(request, 'mytag_cards/business_tag_home.html', context)
    else:
        raise Http404()

    raise Http404()
