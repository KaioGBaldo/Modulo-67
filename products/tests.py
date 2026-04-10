from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Product

class ProductAPITest(APITestCase):
    def setUp(self):
        # Cria 15 produtos para testar a paginação (que definimos como 10 no settings.py)
        # IMPORTANTE: No seu models.py o campo é 'title', não 'name'.
        for i in range(15):
            Product.objects.create(
                title=f"Product {i}", 
                price=10.00,
                active=True
            )

    def test_get_products_list_pagination(self):
        # O nome da rota gerada pelo SimpleRouter/DefaultRouter para listagem 
        # costuma ser 'nome_do_model-list'
        url = reverse('product-list')
        response = self.client.get(url)

        # Verifica se a requisição foi bem-sucedida
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verifica se a resposta tem a chave 'results' (padrão da paginação do DRF)
        self.assertIn('results', response.data)

        # Verifica se trouxe apenas 10 itens (conforme configurado no settings.py)
        self.assertEqual(len(response.data['results']), 10)

    def test_product_content(self):
        """Teste adicional para verificar se os campos estão vindo corretamente"""
        url = reverse('product-list')
        response = self.client.get(url)
        
        # Verifica o primeiro item da lista
        first_product = response.data['results'][0]
        self.assertIn('title', first_product)
        self.assertIn('price', first_product)
