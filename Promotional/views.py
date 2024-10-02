from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from .serializer import PromotionalSerializer
from SalesProduct.models import SalesModel
from rest_framework.response import Response
# Create your views here.

class PromotionalView(ViewSet):
    def list(self,request):
        query = SalesModel.objects.all()
        serializer = PromotionalSerializer(query,many=True)
        return Response(serializer.data)

