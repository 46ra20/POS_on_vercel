from django.shortcuts import render
from rest_framework.viewsets import ViewSet,ModelViewSet
from .models import OwnerModel,BankAccountModel
from .serializer import OwnerSerializer,BankAccountSerializer
# Create your views here.


class OwnerView(ModelViewSet):
    serializer_class=OwnerSerializer
    queryset=OwnerModel.objects.all()

class BankAccountView(ModelViewSet):
    serializer_class = BankAccountSerializer
    queryset = BankAccountModel.objects.all()
    