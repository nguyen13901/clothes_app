from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api_product.models import Product, Category
from api_product.serializers import ProductSerializer


class LatestProductsListView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def list(self, request, *args, **kwargs):
        products = self.get_queryset()[0:4]
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # @action(detail=True, methods=['GET'])
    # def get_detail_product(self, request, *args, **kwargs):
    #     query_set = Product.objects
    #     detail_query = request.query_params.get("q", "").strip()
    #     if detail_query:
    #         q = Q(category_slug=detail_query) & Q(slug=detail_query)
    #         query_set=query_set.filter(q)
    #         serializer = self.get_serializer(query_set)
    #         return Response(serializer.data, status=status.HTTP_200_OK)


# class DetailProductView(ViewSet):
#     queryset = Product.objects
#     serializer_class = ProductSerializer
#
#     def get_object(self, category_slug, product_slug):
#         try:
#             return self.get_queryset().filter(category_slug=category_slug, slug=product_slug)
#         except Product.DoesNotExist:
#             return Response({"error_message": "Product is not exist"}, status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, category_slug, product_slug):
#         product = self.get_object(category_slug, product_slug)
#         serializer = self.get_serializer(product)
#         return Response(serializer.data, status=status.HTTP_200_OK)

class DetailProductView(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class ProductByCategoryView(APIView):
    def get(self, request, category_slug):
        category = Category.objects.filter(name=category_slug)
        if category.exists():
            category = category.first()
            products = category.products.all()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
