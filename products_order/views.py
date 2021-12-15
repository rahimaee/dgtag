from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from django.urls import reverse

from home_products.models import Product
from products_order.forms import UserNewOrderForm
from products_order.models import Order, OrderDetail
from .forms import AddressForm

# bank
from payping.authentication import Bearer
from payping.payment import make_payment_code, verify_payment
from payping.payment import get_url_payment

from mytag.settings import PayPing_Token


@login_required(login_url='/login')
def add_user_order(request):
    new_order_form = UserNewOrderForm(request.POST or None)
    if new_order_form.is_valid():
        order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(owner_id=request.user.id, is_paid=False)
            print(request.user.id)

        product_id = new_order_form.cleaned_data.get('productId')
        product = Product.objects.get_by_id(product_id=product_id)
        count = new_order_form.cleaned_data.get('count')
        up = order.orderdetail_set.filter(product_id=product_id).first()

        if up is not None:
            up.count += count
            up.price = product.price
            up.save()
        else:
            order.orderdetail_set.create(product_id=product_id, price=product.price, count=count)
        return redirect('/')


@login_required(login_url='/login')
def add_shop_on_home(request, *args, **kwargs):
    product_id = kwargs.get('product_id')
    if product_id is not None:
        order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
        if order is None:
            order = Order.objects.create(owner_id=request.user.id, is_paid=False)
        product = Product.objects.get_by_id(product_id=product_id)
        count = 1
        up = order.orderdetail_set.filter(product_id=product_id).first()

        if up is not None:
            up.count += count
            up.price = product.price
            if product.Discount is not None:
                up.Discount = product.Discount
            up.save()
        else:
            order.orderdetail_set.create(product_id=product_id, price=product.price, count=count)
        return redirect('/open-order')


@login_required(login_url='/login')
def user_open_order(request):
    context = {
        'order': None,
        'details': None,
        'total': 0,
    }
    user_id = request.user.id
    all_order_detail = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    all_order_detail = all_order_detail.orderdetail_set.all()
    for pro in all_order_detail:
        if pro is not None:
            pro.price = Product.objects.filter(pk=pro.product.pk).first().price
            pro.save()
    open_order = Order.objects.filter(owner_id=user_id, is_paid=False).first()
    if open_order is not None:
        context['order'] = open_order
        context['details'] = open_order.orderdetail_set.all()
        context['total'] = open_order.get_total_price()
    return render(request, 'products_order/user_open_order.html', context)


@login_required(login_url='account/login')
def update_count(request, *args, **kwargs):
    detail_id = kwargs.get('detail_id')
    order_count = kwargs.get('count')
    if detail_id is not None:
        order_detail = OrderDetail.objects.get_queryset().get(id=detail_id, order__owner_id=request.user.id)
        if order_detail is not None:
            order_detail.count = order_count
            order_detail.save()
            return redirect('/open-order')
    raise Http404()


@login_required(login_url='account/login')
def remove_order_detail(request, *args, **kwargs):
    detail_id = kwargs.get('detail_id')
    if detail_id is not None:
        order_detail = OrderDetail.objects.get_queryset().get(id=detail_id, order__owner_id=request.user.id)
        if order_detail is not None:
            order_detail.delete()
            return redirect('/open-order')
    raise Http404()


@login_required(login_url='account/login')
def add_address_order(request, *args, **kwargs):
    order = Order.objects.filter(owner_id=request.user.id, is_paid=False).first()
    if order is None:
        raise Http404()
    Address_Form = AddressForm(request.POST or None)
    if request.method == "POST":
        if Address_Form.is_valid():
            FullAddress = Address_Form.data.get('FullAddress')
            country = Address_Form.data.get('country')
            province = Address_Form.data.get('province')
            city = Address_Form.data.get('city')
            ZipCode = Address_Form.data.get('ZipCode')
            order.FullAddress = FullAddress
            order.province = province
            order.city = city
            order.country = country
            order.ZipCode = ZipCode
            order.save()
            return send_request(request)
        else:
            raise Http404()

    context = {'Address_Form': Address_Form}

    return render(request, 'products_order/add_address.html', context=context)


def send_request(request):
    userid = request.user.id
    user = User.objects.filter(pk=userid).first()
    if user is None:
        raise Http404()
    order = Order.objects.filter(owner_id=userid, is_paid=False).first()
    if order is None:
        raise Http404()
    description = 'خرید از دی جی تگ'
    header = Bearer(token=PayPing_Token)
    code = make_payment_code(header=header, amount=2000, clientRefId=order.id,
                             payerName=user.get_full_name(),
                             description=description, returnUrl='http://127.0.0.1:8000/verify')
    url = get_url_payment(code=code)
    if url is None:
        raise Http404()

    return redirect(url)


def verify(request):
    ref_id = request.GET.get('refid')
    clientrefid = request.GET.get('clientrefid')
    userid = request.user.id
    user = User.objects.filter(pk=userid).first()
    if user is None:
        raise Http404()
    order = Order.objects.filter(owner_id=userid, is_paid=False).first()
    if order is None:
        raise Http404()
    if clientrefid == '1':
        raise Http404()
    order.ref_id = ref_id
    order.clientrefid = clientrefid
    order.is_paid = True
    order.save()
    header = Bearer(token=PayPing_Token)
    verify_payment(header=header, refid=ref_id, amount=order.get_total_price())

    return HttpResponse('ok')
