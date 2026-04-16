from rest_framework import serializers
from products.models import Product, Order, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug']

class ProductSerializer(serializers.ModelSerializer):
    # 'many=True' é obrigatório porque seu model usa ManyToManyField
    # 'slug_field' faz aparecer o nome da categoria em vez do ID
    category = serializers.SlugRelatedField(
        many=True, 
        slug_field='title', 
        queryset=Category.objects.all()
    )

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'active', 'category']

class OrderSerializer(serializers.ModelSerializer):
    # Opcional: Se quiser mostrar o nome do usuário em vez do ID
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Order
        fields = '__all__'