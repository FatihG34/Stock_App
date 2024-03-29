from django.db import models
from django.contrib.auth.models import User
# from main.settings import AUTH_USER_MODEL


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Firm(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(
        Category, related_name="product_category", on_delete=models.CASCADE)
    brand = models.ForeignKey(
        Brand, related_name="product_brand", on_delete=models.CASCADE)
    stock = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.stock}"


class Transaction(models.Model):
    QUANTITY = (
        ("in", "IN"),
        ("out", "OUT"),
    )
    user = models.ForeignKey(
        User, related_name="transaction_owner", on_delete=models.CASCADE)
    firm = models.ForeignKey(
        Firm, related_name="transaction_owner_firm", on_delete=models.CASCADE)
    transaction = models.CharField(max_length=50, choices=QUANTITY)
    product = models.ForeignKey(
        Product, related_name="transaction_product", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    price_total = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"{self.product} {self.transaction} Stock"

    # @property
    # def price_total(self):
    #     return self.quantity * int(self.price)