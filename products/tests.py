from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Product

class ProductAPITest(APITestCase):
    def setUp(self):
        # Cria 15 produtos para testar a paginação (que definimos como 10)
        for i in range(15):
            Product.objects.create(name=f"Product {i}", price=10.00)

    def test_get_products_list_pagination(self):
        url = reverse('product-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verifica se a resposta tem a chave 'results' (padrão da paginação)
        self.assertIn('results', response.data)
        # Verifica se trouxe apenas 10 itens (conforme configurado no settings)
        self.assertEqual(len(response.data['results']), 10)
