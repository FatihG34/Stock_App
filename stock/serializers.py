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
                  "brand", "brand_id", "stock")



class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields ="__all__"
        # fields = ("id", "name", "phone", "address")


class TransactionSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.IntegerField()
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField()
    firm = serializers.StringRelatedField()
    firm_id = serializers.IntegerField()
    class Meta:
        model = Transaction
        fields = "__all__"
        read_only_fields = ("price_total",)

    def create(self, validated_data):
        # print(validated_data)
        quantity = validated_data["quantity"]
        price = validated_data["price"]
        validated_data["price_total"] = quantity * price
        transaction_stock = Transaction.objects.create(**validated_data)
        # print(transaction_stock)
        return transaction_stock

    def validate(self, data):
        # print(data)
        transaction = data["transaction"]
        product_id = data["product_id"]
        quantity = data["quantity"]
        # stock_core = Product.objects.get(id=product_id)
        stock = Product.objects.filter(id=product_id).values()
        # print(stock_core["stock"])
        if transaction == "in":
            newStock = stock[0]["stock"] + quantity
        elif quantity <= stock[0]["stock"]:
            newStock = stock[0]["stock"] - quantity
        else:
            newStock = stock[0]["stock"]
            raise serializers.ValidationError(
                {
                    "quantity" : "amount of product not enough ..."
                }
            )
        Product.objects.filter(id=product_id).update(stock=newStock)
        return data