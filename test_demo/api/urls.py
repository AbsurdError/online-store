from django.urls import path
from .views import *

urlpatterns = [
    path('products', productsView),
    path('products/<int:pk>', changeProduct),
    path('login', login),
    path('signup', register),
    path('logout', logout),
    path('cart', cartView),
    path('cart/<int:pk>', changeCart),
    path('order', orderView),

]
