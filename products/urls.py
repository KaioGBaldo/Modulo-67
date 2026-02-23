from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet # Importe o novo ViewSet aqui

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')
# ESTA É A LINHA QUE ESTÁ FALTANDO NO SEU CÓDIGO:
router.register(r'order', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]
