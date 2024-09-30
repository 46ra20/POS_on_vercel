from rest_framework.routers import DefaultRouter
from .views import SalesView,SalesSaveView,ReturnView,ReturnViewByKey,DamageView,DamageViewForUser
from django.urls import path,include
router = DefaultRouter()

router.register(r'sales',SalesView)
# router.register(r'return',ReturnView)


urlpatterns = [
    path('sales_save/',SalesSaveView.as_view({'post':'create'})),
    path('return/',ReturnView.as_view({'post':'create'})),
    path('return_by_key/<search_key>/',ReturnViewByKey.as_view({'get':'list'})),
    path('damage_get/',DamageViewForUser.as_view({'get':'list'})),
    path('damage_add/',DamageView.as_view({'post':'create'})),
    path('',include(router.urls))
]