from django.db import models
from django.contrib.auth import get_user_model
from goods.models import Book

# Create your models here.
User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="carts", blank=True, null=True
    )
    created = models.DateTimeField(
        verbose_name="Дата создания", auto_now_add=True, auto_now=False, blank=True, null=True
    )
    updated = models.DateTimeField(
        verbose_name="Дата создания", auto_now_add=False, auto_now=True, blank=True, null=True 
    )

    def order_price(self):
        order = self.items.all()
        total_order_price = 0
        for item in order:
            total_order_price += item.total_price_per_item
        return total_order_price

    def __str__(self) -> str:
        return f"Cart for №{self.pk} {self.user}"

class OrderInCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT, verbose_name="Корзина", related_name="items")
    item = models.ForeignKey(Book, on_delete=models.PROTECT, verbose_name="Книга", related_name="item_in_cart")
    quantity = models.IntegerField(verbose_name="Количество", default=1)
    price_per_item = models.DecimalField(verbose_name="Цена", max_digits=7, decimal_places=2)


    @property
    def total_price_per_item(self):
        return self.quantity * self.price_per_item

    def __str__(self):
        return f'{self.pk} Книга {self.item} в корзине {self.cart} в количестве {self.quantity} штук(и)'

class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT, related_name="cart")
    phone = models.CharField(verbose_name="Телефон", max_length=13)
    address = models.CharField(verbose_name="Адрес доставки", max_length=100)

    def __str__(self):
        return f" Заказ №{self.pk}"
       