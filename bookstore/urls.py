from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products import views # Importa as views do seu app 'products'

router = DefaultRouter()
router.register(r'product', views.ProductViewSet, basename='product')
router.register(r'category', views.CategoryViewSet, basename='category')
# ADICIONE ESTA LINHA:
router.register(r'order', views.OrderViewSet, basename='order')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), # Suas rotas ficarão em api/order/
]
