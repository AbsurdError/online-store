from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Products)
admin.site.register(Carts)
admin.site.register(Order)
