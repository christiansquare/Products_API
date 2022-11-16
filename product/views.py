from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import Productserializer
from .models import Product

@api_view(['GET'])
def product_list(request):

    product = Product.objects.all()

    serializer = Productserializer(product, many=True)

    return Response(serializer.data)
