from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet # Certifique-se de importar os outros se criar as views

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')
# Se você criar as ViewSets para os outros, registre-os aqui:
# router.register(r'category', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]
