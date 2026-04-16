from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet # Certifique-se de importar a OrderViewSet!

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')
router.register(r'order', OrderViewSet, basename='order') # O nome aqui define a URL

urlpatterns = [
    path('', include(router.urls)),
]