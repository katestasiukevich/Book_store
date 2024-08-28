from django.contrib import admin
from django.contrib.admin.options import ModelAdmin, TabularInline, StackedInline
from .models import Cart, OrderInCart, Order


# Register your models here.
class OrderInline(StackedInline):
    extra = 3
    model = Order

class OrderAdmin(ModelAdmin):
    inlines = OrderInline,
    fields = ('phone', 'address')


admin.site.register(Cart)
admin.site.register(OrderInCart)
admin.site.register(Order)
