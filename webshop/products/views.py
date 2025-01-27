from urllib import request

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product


@api_view(http_method_names=['GET', 'POST'])
def product_list_create_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        list_ = ProductSerializer(instance=products, many=True).data

     # list_ = []
     # for i in products:
     #     list_.append({
     #         'id': i.id,
     #         'title': i.title,
     #         'description': i.description,
     #         'price': i.price,
     #     })

        return Response(data=list_)
    elif request.method == 'POST':
        return Response()

@api_view(['GET'])
def product_list_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,data={'error': 'Product not found!'})
    data = ProductSerializer(instance=product).data
    return Response(data=data)