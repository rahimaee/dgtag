from django.shortcuts import render, redirect
from .models import Newsletters
from .forms import NewslettersForm


# Create your views here.


def news_letters_partial_view(request, *args, **kwargs):
    news_lettersForm = NewslettersForm(request.POST or None)
    if request.POST:
        if 'news' in request.POST:
            MyNewsletters = Newsletters()
            MyNewsletters.Email = news_lettersForm.data.get('email')
            MyNewsletters.save()

    context = {
        'news_lettersForm': news_lettersForm
    }
    return render(request, 'home_newsletters/Newsletters_partial_view.html', context)
