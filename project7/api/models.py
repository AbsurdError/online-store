from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    fio = models.CharField(max_length=25)
    password = models.CharField(max_length=20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'fio']

class Products(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class Carts(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Orders(models.Model):
    products = models.ManyToManyField(Products)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_price = models.DecimalField(max_digits=7, decimal_places=2)

