from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products import views

router = DefaultRouter()
router.register(r'product', views.ProductViewSet, basename='product')
router.register(r'order', views.OrderViewSet, basename='order')
router.register(r'category', views.CategoryViewSet, basename='category')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]