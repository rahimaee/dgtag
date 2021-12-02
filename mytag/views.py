from django.shortcuts import render

from home_comments.forms import CommentForm
from home_comments.models import Comments


def home_page(request, *args, **kwargs):
    comment_form = CommentForm(request.POST or None)
    context = {
        'comment_form': comment_form
    }
    return render(request, 'home_page.html', context)
