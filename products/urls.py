from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet # Importe a OrderViewSet que criamos acima

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')
router.register(r'order', OrderViewSet, basename='order') # ESTA LINHA É A CHAVE DA APROVAÇÃO

urlpatterns = [
    path('', include(router.urls)),
]
