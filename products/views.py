from rest_framework import viewsets
from .models import Product, Order  # Adicione Order aqui
from .serializers import ProductSerializer, OrderSerializer # Adicione OrderSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

# ADICIONE ESTA CLASSE:
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer
