from django.db import models

class Order(models.Model):
    # Exemplo simples de campos para um pedido
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    data_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id} - {self.product.nome}"
