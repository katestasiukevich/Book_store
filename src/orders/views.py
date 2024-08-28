from urllib import request
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from . import models, forms
from acc import views as acc_view


# Create your views here.
def update_item_in_cart(key, quantity):
    item_in_cart_id = int(key.split("_")[1])
    item_in_cart = models.OrderInCart.objects.get(pk=item_in_cart_id)
    if int(quantity) == 0:
        item_in_cart.delete()
    else:
        item_in_cart.quantity = int(quantity)
        item_in_cart.save()
    item_in_cart.quantity = int(quantity)

def get_or_create_current_cart(request):
    cart_id = request.session.get("cart_id", None)
    if request.user.is_anonymous:
        user = None
    else:
        user = request.user
    cart, created = models.Cart.objects.get_or_create(
        pk=cart_id,
        defaults={'user': user}
    )
    if created:
        request.session["cart_id"] = cart.pk
    return cart

def get_current_cart(request):
    cart_id = request.session.get("cart_id", None)
    cart = models.Cart.objects.filter(pk=cart_id)
    if cart:
        cart = cart[0]
    else:
        cart = bool(cart)
    return cart

def add_item_to_cart(request):
    item_id = int(request.POST.get("item_id"))
    item = models.Book.objects.get(pk=item_id)
    price = item.price
    quantity = int(request.POST.get("quantity"))
    cart = get_or_create_current_cart(request)
    item_in_cart, created = models.OrderInCart.objects.get_or_create(
        cart=cart,
        item=item,
        defaults={'quantity': quantity,
                  'price_per_item': price,
                  }
    )
    if not created:
        current_quantity = item_in_cart.quantity
        item_in_cart.quantity = current_quantity + quantity
        item_in_cart.save()


def view_cart(request):
    cart = get_or_create_current_cart(request)
    context = {'cart': cart}
    return render(request, template_name="orders/view_cart.html", context=context)

def add_item_to_cart_view(request):
    if request.method == "POST":
        add_item_to_cart(request)
    return HttpResponseRedirect(reverse_lazy("orders:view-cart"))

def create_order(request):
    cart = get_current_cart(request)
    return cart


def evaluate_cart(request):
    if request.method == "POST":
        action = None
        for key, value in request.POST.items():
            if key[0:4] == "quan":
                update_item_in_cart(key, value)
            if key[0:4] == "acti":
                action = value
        if action == "update":
            return HttpResponseRedirect(reverse_lazy("orders:view-cart"))
        return HttpResponseRedirect(reverse_lazy("orders:view-order-created"))

def get_customer_phone(user):
    code = user.profile.code
    phone = user.profile.phone
    return "+375" + str(code) + str(phone)

def get_customer_address(user):
    address = user.profile.address1
    return address

class CreateOrderView(generic.CreateView):
    model = models.Order
    form_class = forms.CreateOrderForm
    template_name = "orders/create_order.html"
    success_url = reverse_lazy("orders:created-page")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = get_current_cart(self.request)
        return context
    
    def get_form(self, **kwargs):
        form = super().get_form(**kwargs)
        if self.request.user.is_authenticated:
            form.fields['phone'].initial = get_customer_phone(self.request.user)
            form.fields['address'].initial = get_customer_address(self.request.user)
        # else:
        #     form.fields['phone']
        #     form.fields['address']

        return form
    
    def form_valid(self, form):
        order = form.save(commit=False)
        order.cart = get_current_cart(self.request)
        order.save()
        self.object = order
        return HttpResponseRedirect(self.get_success_url())

    
class OrderCreatedView(generic.TemplateView):
    template_name = "orders/created.html"

    