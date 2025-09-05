from django.urls import path
from .views import PingingView


urlpatterns = [
    path('ping/', PingingView.as_view(), name='ping'),
]