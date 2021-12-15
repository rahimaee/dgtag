from django.shortcuts import render

from home_comments.forms import CommentForm
from home_comments.models import Comments
from home_products.models import Product


def home_page(request, *args, **kwargs):
    comment_form = CommentForm(request.POST or None)
    AllProduct = Product.objects.filter(is_active=True).all()
    context = {
        'comment_form': comment_form,
        'AllProduct': AllProduct
    }
    return render(request, 'home_page.html', context)


def test(request):
    context = {}
    return render(request, 'testshop.html', context)


def shop(request):
    context = {}
    return render(request, 'shop.html', context)
