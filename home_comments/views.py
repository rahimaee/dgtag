from django.shortcuts import render, redirect
from home_comments.forms import CommentForm
from .models import Comments


# Create your views here.

def comment_partial_view(request, *args, **kwargs):
    comment_form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if 'comment_form' in request.POST:
            print('comment_form')

    context = {
        'comment_form': comment_form
    }
    return render(request, 'home_comments/comment_partial_view.html', context)
