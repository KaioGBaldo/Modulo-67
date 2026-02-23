from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet # Verifique se ambos estão importados

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')
# A correção solicitada pelo professor está nesta linha:
router.register(r'order', OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]
