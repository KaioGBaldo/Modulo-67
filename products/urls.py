from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

# O Router do DRF cria automaticamente as rotas de GET, POST, PUT e DELETE
router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]
