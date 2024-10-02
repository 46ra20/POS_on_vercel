from django.shortcuts import render
from .models import PaymentModel,ExpensesModel
from .serializer import PaymentSerializer,PaymentUpdateSerializer,ExpanseSerializer,ExpanseSerializerView
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import response
# Create your views here.

class PaymentView(ViewSet):
    def list(self,request,key):
        if key=='all':
            query = PaymentModel.objects.all()
        else:
            query = PaymentModel.objects.filter(company_name__icontains=key)
        serializer = PaymentSerializer(query,many=True)
        return Response(serializer.data)

class PaymentUpdateView(APIView):
    def patch(self,request,pk=None):
        payment = PaymentModel.objects.get(pk=pk)
        # print('payment',payment,'\n data',request.data,'\n pk',pk)
        serializer = PaymentUpdateSerializer(data=request.data,partial=True)
        if serializer.is_valid():
            print('from is valid')
            serializer.save()
            print(self.request,request.data,pk)
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors)
    

class ExpanseView(ViewSet):
    def list(self,request):
        query = ExpensesModel.objects.all()
        serializer = ExpanseSerializerView(query,many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer = ExpanseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Successfully added expanse','type':'success','data':serializer.data})
        return Response(serializer.errors)