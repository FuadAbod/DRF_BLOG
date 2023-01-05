from django.urls import path
from .views import ListCreateAPIVIEW, UpdateDestroyVIEW

urlpatterns = [
    path('posts', ListCreateAPIVIEW.as_view(), name='api-cr'),
    path('posts/<int:pk>/', UpdateDestroyVIEW.as_view(), name='api-ud'),
]