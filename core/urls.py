from django.urls import path
from .views import *


urlpatterns = [
    path('create-product/', CreateProductView.as_view(), name='create-product'),
    path('list-products/', ListProductAPIView.as_view(), name='list-products'),
]