from django.shortcuts import render
from home_products.models import Product


def home_page(request, *args, **kwargs):
    AllProduct = Product.objects.filter(is_active=True).all()
    AllProductsDiscount = Product.objects.filter(is_active=True, DiscountActive=True).all()
    context = {

        'AllProduct': AllProduct,
        'AllProductsDiscount': AllProductsDiscount
    }
    return render(request, 'home_page.html', context)


