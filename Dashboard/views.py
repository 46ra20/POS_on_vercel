from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PLDModel
from .serializer import PLDSerializer
from datetime import datetime
from django.db.models import Sum
from django.http import JsonResponse
# Create your views here.

class PDLView(APIView):

    def get(self, request, get_date, type):
        newDate = datetime.strptime(get_date, "%Y-%m-%dT%H:%M:%S.%fZ")
        filter_kwargs = {}
        if type == '0':  
            filter_kwargs['date__day'] = newDate.day
            filter_kwargs['date__month'] = newDate.month
            filter_kwargs['date__year'] = newDate.year
        elif type == '1': 
            filter_kwargs['date__month'] = newDate.month
            filter_kwargs['date__year'] = newDate.year
        elif type == '2':  
            filter_kwargs['date__year'] = newDate.year

        result = PLDModel.objects.filter(**filter_kwargs).aggregate(
            total_profit=Sum('profit') or 0.00, 
            total_loss=Sum('loss') or 0.00, 
            total_damage=Sum('damage') or 0.00
        )
        
        data = {
            'profit': result['total_profit'] or 0.00,
            'loss': result['total_loss'] or 0.00,
            'damage': result['total_damage'] or 0.00
        }

        return Response(data)

    # def get(self,request,get_date,type):
    #     newDate = datetime.strptime(get_date,"%Y-%m-%dT%H:%M:%S.%fZ")
    #     print(type)
    #     data = {'profit':0.00,'loss':0.00,'damage':0.00}
    #     if(type=='0'):
    #         query = PLDModel.objects.filter(date__day=newDate.day)
    #     elif(type=='1'):
    #         query = PLDModel.objects.filter(date__month=newDate.month)
    #     elif(type=='2'):
    #         query = PLDModel.objects.filter(date__year=newDate.year)
    #     else:
    #         query = PLDModel.objects.all()

        
        
        
    #     serializer = PLDSerializer(query,many=True)
    #     for item in serializer.data:
    #         data['profit']=data['profit']+float(item['profit'])
    #         data['loss']=data['loss']+float(item['loss'])
    #         data['damage']=data['damage']+float(item['damage'])
        
    #     # serializer.is_valid()
    #     # print(serializer.errors)
    #     print(data)

    #     return Response(data)
    # def create(self,request,date):
    #     query = PLDModel.objects.all()
    #     serializer = PLDSerializer(query,many=True)
    #     return Response(serializer.data)
    
