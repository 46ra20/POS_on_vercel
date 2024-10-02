from rest_framework import serializers
from .models import PaymentModel,ExpensesModel
from Product.models import PurchaseModel

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model= PaymentModel
        # fields=['id','company_name','total_price','cash','outstanding']
        fields='__all__'
        

class PaymentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model= PaymentModel
        fields='__all__'
    
    def save(self,*args,**kwargs):
        instance = super().save(*args,**kwargs)
        print(instance.purchase,instance,instance.total_price)
        payment_update = PurchaseModel.objects.get(pk=instance.purchase.id)
        payment_update.outstanding-=instance.cash
        instance.outstanding-=instance.cash
        payment_update.save()
        instance.save()

class ExpanseSerializer(serializers.ModelSerializer):
    class Meta: 
        model=ExpensesModel
        fields='__all__'

class ExpanseSerializerView(serializers.ModelSerializer):
    class Meta: 
        model=ExpensesModel
        fields=['for_what','amount','cash','outstanding']
        