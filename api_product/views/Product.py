from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api_product.models import Product
from api_product.serializers import ProductSerializer


class LatestProductsListView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get(self, request, format=None):
        products = self.get_queryset()[0:4]
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDetailView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category_slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = self.get_serializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)