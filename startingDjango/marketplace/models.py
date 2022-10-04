from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(User):
    cart_id = models.IntegerField()


class Brand(models.Model):
    name = models.CharField(max_length=15)

class Category(models.Model):
    name = models.CharField(max_length=15)

class Item(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

class Cart(models.Model):
    customer_id = models.IntegerField()
    item_id = models.IntegerField()
    items = models.ManyToManyField(Item)

