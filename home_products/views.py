import itertools

from django.http import Http404
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from home_products.models import Product, Gallery
from home_products_category.models import Category


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


class ProductsList(ListView):
    template_name = 'home_products/products_list.html'

    # paginate_by = 12

    def get_queryset(self):
        return None


def products_detail(request, *args, **kwargs):
    product_name = kwargs['name']
    product_id = kwargs['productId']
    # new_order_form = UserNewOrderForm(request.POST or None, initial={'productId': product_id})
    product = Product.objects.get_by_id(product_id)
    if product is None or not product.is_active:
        raise Http404()

    tag = product.Tag.all()
    gallery = Gallery.objects.filter(product_id=product_id).all()
    category = Category.objects.all()
    gallery = list(my_grouper(3, gallery))
    context = {
        'product': product,
        'tag': tag,
        'category': category,
        'gallery': gallery,
        # 'new_order_form': new_order_form,
    }

    return render(request, 'home_products/products_detail.html', context)


