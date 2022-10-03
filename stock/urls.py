from django.urls import path
from .views import home, CategoryView, BrandView, ProductView, FirmView, TransactionView
from rest_framework import routers

router = routers.DefaultRouter()
router.register("category", CategoryView)
router.register("brand", BrandView)
router.register("product", ProductView)
router.register("firm", FirmView)
router.register("transaction", TransactionView)

urlpatterns = [
    path('', home, name='home'),
]
urlpatterns += router.urls
