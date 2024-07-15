from .views import *
from django.urls import path

urlpatterns = [
    path('products', productsView),
    path('login', login),
    path('signup', register),
    path('product', createProduct),
    path('product/<int:pk>', createProduct),
    path('logout', logout),
    path('cart', cartView),
    path('cart/<int:pk>', changeCart),
    path('order', orderView)

]
