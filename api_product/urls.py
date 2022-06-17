# from core.api_product import views
from django.urls import path, include
from rest_framework import routers

from api_product import views

router = routers.DefaultRouter()
router.register("products", views.LatestProductsListView, basename="product")

urlpatterns = [
    path("", include(router.urls)),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.DetailProductView.as_view(), name="detail_product"),
]
