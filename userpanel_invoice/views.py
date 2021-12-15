from django.http import Http404
from django.shortcuts import render

# Create your views here.
from products_order.models import Order


def all_invoice(request):
    userid = request.user.id
    if userid is None:
        raise Http404()
    all_order = Order.objects.filter(owner_id=userid, is_paid=False).all()
    context = {
        'all_order': all_order
    }
    return render(request, 'userpanel_invoice/user_all_invoice.html', context)


def invoice_detail(request, *args, **kwargs):
    context = {}
    return render(request, 'userpanel_invoice/user_invoice_detail.html', context)
