from django.db import models
from django.contrib.auth.models import User


class Currency(models.Model):
    name = models.CharField(max_length=10)


class Store(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    administrator = models.ForeignKey(User, on_delete=models.CASCADE,
                                      related_name='admin_stores')
    managers = models.ManyToManyField(User, related_name='managed_stores')


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE,
                                 related_name='orders')
    products = models.ManyToManyField(Product, through='OrderItem')


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

