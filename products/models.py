from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    active = models.BooleanField(default=True)
    # Um produto pode ter várias categorias e uma categoria vários produtos
    category = models.ManyToManyField(Category, related_name="products", blank=True)

    def __str__(self):
        return self.title

class Order(models.Model):
    # Relaciona o pedido com um utilizador do sistema
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Um pedido pode ter vários produtos
    product = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id} - {self.user.username}"