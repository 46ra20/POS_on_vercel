from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import OwnerView,BankAccountView

router = DefaultRouter()
router.register(r'owner_list',OwnerView)
router.register(r'bank_account',BankAccountView)


urlpatterns = [
    path('',include(router.urls)),
    # path('',include(router.urls)),
]
