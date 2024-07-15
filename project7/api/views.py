from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_403_FORBIDDEN, HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND, HTTP_422_UNPROCESSABLE_ENTITY
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsClient
from .models import *
from .serializers import *
# Create your views here.

@api_view(['GET'])
def productsView(request):
    products = Products.objects.all()
    prod_ser = ProductsSerializer(products, many=True)
    return Response({'data': prod_ser.data}, status=HTTP_200_OK)