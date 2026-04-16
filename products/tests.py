from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from products.models import Product, Order

class Module67APITest(APITestCase):

    def setUp(self):
        # 1. Criar um usuário para associar aos pedidos
        self.user = User.objects.create_user(username='tester', password='password123')
        
        # 2. Criar 15 produtos (para testar a paginação de 10 itens)
        self.products = []
        for i in range(15):
            p = Product.objects.create(
                title=f"Product {i}",
                price=10.00 + i,
                active=True
            )
            self.products.append(p)

        # 3. Criar 12 pedidos (para testar a paginação em Order também)
        for i in range(12):
            order = Order.objects.create(user=self.user)
            order.product.add(self.products[0]) # Adiciona ao menos um produto

    def test_product_pagination(self):
        """Verifica se a rota de Product existe e se a paginação funciona"""
        url = reverse('product-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verifica se o DRF paginou (presença da chave 'results')
        self.assertIn('results', response.data)
        # Verifica se limitou a 10 produtos (conforme configurado no seu settings.py)
        self.assertEqual(len(response.data['results']), 10)

    def test_order_route_exists_and_paginates(self):
        """
        O PONTO CRÍTICO: Verifica se a rota de Order que o tutor pediu existe
        e se também está paginada.
        """
        url = reverse('order-list')
        response = self.client.get(url)
        
        # Se este teste falhar, a rota não foi registrada no urls.py
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verifica se a paginação está ativa em Order
        self.assertIn('results', response.data)
        # Verifica se trouxe os itens (10 por página)
        self.assertEqual(len(response.data['results']), 10)

    def test_order_content(self):
        """Verifica se o conteúdo do pedido está correto (User e Products)"""
        url = reverse('order-list')
        response = self.client.get(url)
        
        # Verifica se o campo 'user' está vindo (como você usou ReadOnlyField no serializer)
        first_order = response.data['results'][0]
        self.assertIn('user', first_order)
        self.assertIn('product', first_order)
