from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet,ViewSet
from .models import SalesModel,ReturnModel,DamageModel
from .serializer import SalesSerializers,ReturnSerializer,ReturnSerializerByKey,DamageSerializer,DamageSerializerForUser
# Create your views here.

class SalesView(ModelViewSet):
    
    serializer_class=SalesSerializers
    queryset = SalesModel.objects.all()

class ReturnView(ViewSet):
    def create(self,request):
        serializer = ReturnSerializer(data=request.data)
        print(request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ReturnViewByKey(ViewSet):
    def list(self,request,search_key):
        print(search_key)
        if(search_key=='all' or search_key=='All'):
            query = ReturnModel.objects.all()
        else:
            query=ReturnModel.objects.filter(product__product_name=search_key)
        serializer = ReturnSerializerByKey(query,many=True) 
        return Response(serializer.data)


class SalesSaveView(ViewSet):
    def create(self,request):
        # print(request.data,'\n')
        serializer = SalesSerializers(data=request.data,required=False)
        # serializer.is_valid()
        # print('serializer data',serializer.data,'\n')
        # print(serializer.errors)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Sales update successfully.','type':'success','data':serializer.data})
        return Response(serializer.errors)
    

class DamageView(ViewSet):
    def create(self,request):
        serializer = DamageSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({'message':'Sales update successfully.','type':'success','data':serializer.data})
        return Response(serializer.errors)

class DamageViewForUser(ViewSet):
    def list(self,request):
        query = DamageModel.objects.all()
        serializer = DamageSerializerForUser(query,many=True)
        return Response(serializer.data)