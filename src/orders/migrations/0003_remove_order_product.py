# Generated by Django 4.2.13 on 2024-08-27 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
    ]
