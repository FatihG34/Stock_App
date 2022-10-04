from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from rest_framework import permissions

from stock.models import Brand, Category, Firm, Product, Transaction
from stock.serializers import BrandSerializer, CategorySerializer, FirmSerializer, TransactionSerializer

# Create your views here.


def home(request):
    return HttpResponse("<h1>Here is Stock Page</h1>")

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = BrandSerializer

class FirmView(viewsets.ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer

class TransactionView(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer