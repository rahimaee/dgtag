from django.shortcuts import render
from home_products.models import Product


def home_page(request, *args, **kwargs):
    AllProduct = Product.objects.filter(is_active=True).all()
    context = {

        'AllProduct': AllProduct
    }
    return render(request, 'home_page.html', context)


