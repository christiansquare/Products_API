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

@api_view(['GET'])
def product_detail(request, pk):
    try:
     product = Product.objects.get(pk=pk)
     serializer = Productserializer(product);
     return Response(serializer.data)

    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
