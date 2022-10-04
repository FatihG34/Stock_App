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
    # amount_stock = serializers.SerializerMethodField()
    category = serializers.StringRelatedField(read_only=True)
    category_id = serializers.IntegerField()
    brand = serializers.StringRelatedField(read_only=True)
    brand_id = serializers.IntegerField()
    class Meta:
        model = Product
        fields = ("id", "name", "category", "category_id",
                  "brand", "brand_id", "stock", "stock_amount")
    
    # def get_amount_stock(self, obj):
    #     if self.transaction_product.transaction == 'in':
    #         obj.stock += obj.transaction_product.quantity
    #     else:
    #         obj.stock -= obj.transaction_product.quantity


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
                  "product_id", "quantity", "price", "price_total")
