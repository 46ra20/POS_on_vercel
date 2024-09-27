from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet,ViewSet
from .models import SalesModel
from .serializer import SalesSerializers
# Create your views here.

class SalesView(ModelViewSet):
    
    serializer_class=SalesSerializers
    queryset = SalesModel.objects.all()


class SalesSaveView(ViewSet):
    def create(self,request):
        # print(request.data,'\n')
        serializer = SalesSerializers(data=request.data,required=False)
        # serializer.is_valid()
        # print('serializer data',serializer.data,'\n')
        print(serializer.errors)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Sales update successfully.','type':'success'})
        return Response(serializer.errors)