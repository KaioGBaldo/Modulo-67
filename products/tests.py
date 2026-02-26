from django.test import TestCase
from django.contrib.auth.models import User
from .models import Product, Category, Order

class IntegridadeTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='kaio', password='123')
        self.cat = Category.objects.create(title='Hardware')
        self.prod = Product.objects.create(title='Teclado', price=150.0)
        self.prod.category.add(self.cat)

    def test_integridade_modelos(self):
        order = Order.objects.create(user=self.user)
        order.product.add(self.prod)
        self.assertEqual(self.prod.category.count(), 1)
        self.assertEqual(order.product.first().title, 'Teclado')
        self.assertEqual(order.user.username, 'kaio')