from django.urls import path, include

from api_product import views


urlpatterns = [
<<<<<<< HEAD
    path("", include(router.urls)),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.DetailProductView.as_view(),
         name="detail_product"),
    path('products/<slug:category_slug>', views.CategoryProductView.as_view(), name="product_by_category"),
=======
    path('products/', views.LatestProductsListView.as_view()),
    path('products/search/', views.search),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.DetailProductView.as_view(),
         name="detail_product"),
    path('products/<slug:category_slug>/', views.CategoryProductView.as_view(), name="product_by_category"),
>>>>>>> Implement category view 17.06.2022
]
