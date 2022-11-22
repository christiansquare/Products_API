from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import Productserializer
from .models import Product

@api_view(['GET','POST'])
def product_list(request):

  if request.method == 'GET':
    product = Product.objects.all()
    serializer = Productserializer(product, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = Productserializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','Put','DELETE'])
def product_detail(request, pk):
    product = get_object_or_404(Product,pk=pk)
    if request.method == "GET":
     serializer = Productserializer(product);
     return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = Productserializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    