import datetime

from django.db import transaction, IntegrityError
# Create your views here.
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView

from mytag_cards.models import Card
from userpanel_mytag.forms import CardForm, CardFormset, CardSocialNetworkFormset


class HomepageView(TemplateView):
    template_name = "userpanel_mytag/base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Cards'] = Card.objects.filter(created_by=self.request.user)
        return context


class MyTagDetailView(DetailView):
    model = Card
    template_name = 'userpanel_mytag/user_panel_mytag_detail.html'

    def get_context_data(self, **kwargs):
        user_card = Card.objects.filter(pk=self.object.pk).first()
        if user_card is not None:
            if self.request.user == user_card.created_by:
                context = super(MyTagDetailView, self).get_context_data(**kwargs)
                return context
            else:
                raise Http404()
        raise Http404()


class MyTagCreate(CreateView):
    model = Card
    template_name = 'userpanel_mytag/user_panel_mytag_create.html'
    form_class = CardForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(MyTagCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['titles'] = CardFormset(self.request.POST)
            data['cards'] = CardSocialNetworkFormset(self.request.POST)
        else:
            data['titles'] = CardFormset()
            data['cards'] = CardSocialNetworkFormset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        titles = context['titles']
        cards = context['cards']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            form.instance.CardId = 222
            form.instance.BuildTime = datetime.datetime.now()
            form.instance.TypeOfCard_id = 1
            self.object = form.save()
            if titles.is_valid():
                titles.instance = self.object
                titles.save()
            if cards.is_valid():
                cards.instance = self.object
                cards.save()
        return super(MyTagCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('userpanel_mytag:detail', kwargs={'pk': self.object.pk})


class MyTagUpdate(UpdateView):
    model = Card
    form_class = CardForm
    template_name = 'userpanel_mytag/user_panel_mytag_create.html'

    def get_context_data(self, **kwargs):
        user_card = Card.objects.filter(pk=self.object.pk).first()
        if user_card is not None:
            if self.request.user == user_card.created_by:
                data = super(MyTagUpdate, self).get_context_data(**kwargs)
                if self.request.POST:
                    data['titles'] = CardFormset(self.request.POST, instance=self.object)
                    data['cards'] = CardSocialNetworkFormset(self.request.POST, instance=self.object)
                else:
                    data['titles'] = CardFormset(instance=self.object)
                    data['cards'] = CardSocialNetworkFormset(instance=self.object)
                return data
            else:
                raise Http404()
        else:
            raise Http404()

    def form_valid(self, form):
        context = self.get_context_data()
        titles = context['titles']
        cards = context['cards']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if titles.is_valid():
                titles.instance = self.object
                titles.save()
            if cards.is_valid():
                cards.instance = self.object
                cards.save()
        return super(MyTagUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('userpanel_mytag:homepage')


class MyTagDelete(DeleteView):
    model = Card
    template_name = 'userpanel_mytag/user_panel_confirm_delete.html'
    success_url = reverse_lazy('userpanel_mytag:homepage')
