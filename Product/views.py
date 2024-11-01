from django.shortcuts import render
from django.db.models import Q
from .serializer import ProductSerializer,CategorySerializer,BrandSerializer,ProductSearchByNameSerializer,UnitSerializer,PurchaseSerializer,PurchaseSerializerForView,StockSerializer
from .models import ProductModel,CategoryModel,BrandModel,UnitModel,PurchaseModel

from rest_framework.views import APIView,Response
from rest_framework.viewsets import ViewSet,ModelViewSet
# Create your views here.

class CategoryView(ModelViewSet):
    # class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = CategorySerializer
    queryset = CategoryModel.objects.all()

class BrandView(ModelViewSet):
    serializer_class=BrandSerializer
    queryset=BrandModel.objects.all()

class UnitView(ModelViewSet):
    serializer_class=UnitSerializer
    queryset=UnitModel.objects.all()
    

class ProductView(ViewSet):
    def list(self,request,key):
        if(key!='all'):
            query = ProductModel.objects.filter(product_name__icontains=key,product_code__icontains=key.upper())
        else:
            query= ProductModel.objects.all()
        serializer = ProductSerializer(query,many=True)
        return Response(serializer.data)
    
    def create(self,request,userId):
        serializer = ProductSerializer(data = request.data,required=False)
        print(serializer.is_valid())
        # print(serializer.data,request.data)
        print(serializer.errors)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Your product add successfully,','type':'success'})
        return Response({'message':'Something wrong please try agin,','type':'danger'})
    
    def update(self,request,id):
        serializer = ProductSerializer(data=request.data,partial=True)
        print(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Your product information update successfully,','type':'success'})
        return Response({'message':'Something wrong please try agin,','type':'danger'})

    def destroy(self,request,id):
        product = ProductModel.objects.get(pk=id)
        print(id,product)
        if product.delete():
            return Response({'message':'Your product delete successfully,','type':'success'})
        return Response({'message':'Something wrong please try agin,','type':'danger'})

class ProductSearchByName(ViewSet):
    def list(self,request,key=None):
        print(key)
        if key:
            query = ProductModel.objects.filter((Q(product_name__icontains=key)|Q(product_code__icontains=key.upper()))&Q(quantity__gt=0))
            # query = ProductModel.objects.all()
            serializer = ProductSearchByNameSerializer(query,many=True)
            print(query,serializer.data)
            return Response(serializer.data)
        

class PurchaseView(ViewSet):
    def create(self,request):
        serializer = PurchaseSerializer(data=request.data)

        if(serializer.is_valid()):
            serializer.save()
            return Response({'message':'Product successfully purchased','data':serializer.data})
        return Response(serializer.errors)
    
    def list(self,request):
        query = PurchaseModel.objects.all()
        serializer = PurchaseSerializerForView(query,many=True)
        return Response(serializer.data)
    
class StockView(ViewSet):
    def list(self,request):
        query = PurchaseModel.objects.all()
        serializer = StockSerializer(query,many=True)
        return Response(serializer.data)