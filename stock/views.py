from rest_framework import viewsets, filters
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from stock.models import Brand, Category, Firm, Product, Transaction
from stock.serializers import BrandSerializer, CategorySerializer, FirmSerializer, TransactionSerializer, ProductSerializer

# Create your views here.

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.DjangoModelPermissions]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]


class BrandView(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
    permission_classes = [permissions.DjangoModelPermissions]

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["name"]
    filterset_fields = ("category", "brand")
    permission_classes = [permissions.DjangoModelPermissions]


class FirmView(viewsets.ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
    permission_classes = [permissions.DjangoModelPermissions]

class TransactionView(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["firm"]
    permission_classes = [permissions.DjangoModelPermissions]
