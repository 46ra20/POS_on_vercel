from rest_framework.routers import DefaultRouter
from .views import SalesView,SalesSaveView
from django.urls import path,include
router = DefaultRouter()

router.register(r'sales',SalesView)

urlpatterns = [
    path('sales_save/',SalesSaveView.as_view({'post':'create'})),
    path('',include(router.urls))
]