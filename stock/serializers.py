from rest_framework import serializers
from .models import Category, Product, Brand, Firm, Transaction


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ("id", "name")


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    category_id = serializers.IntegerField()
    brand = serializers.StringRelatedField(read_only=True)
    brand_id = serializers.IntegerField()
    class Meta:
        model = Product
        fields = ("id", "name", "category", "category_id",
                  "brand", "brand_id", "stock")


class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields ="__all__"
        # fields = ("id", "name", "phone", "address")


class TransactionSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField(read_only=True)
    product_id = serializers.IntegerField()
    class Meta:
        model = Transaction
        fields = ("id", "firm", "transaction", "product",
                  "product_id", "quantity", "price")
