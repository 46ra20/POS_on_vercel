from rest_framework import serializers
from .models import SalesModel,ProductModel,ReturnModel,DamageModel
from Dashboard.models import PLDModel

class SalesSerializers(serializers.ModelSerializer):
    class Meta:
        model = SalesModel
        fields = '__all__'

    def save(self,*args, **kwargs):
        # print(self.data)
        instance = super().save(*args,**kwargs)
        quantity = self.data['sales_quantity'].split(',')
        items = self.data['sales_item']
        i=0
        profit = 0
        loss=0
        # newPld = PLDModel
        for item in items:
            product = ProductModel.objects.get(id=item)
            product.quantity-=int(quantity[i])
            if(product.seals_price>=product.purchase_price):
                profit=profit+int((product.seals_price-product.purchase_price)*int(quantity[i]))
            elif product.seals_price<product.purchase_price:
                loss=loss+int((product.purchase_price-product.seals_price)* int(quantity[i]))
            i+=1
            product.save()
        PLDModel.objects.create(profit=profit,loss=loss,damage=0)

class ReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReturnModel
        fields = '__all__'

class ReturnSerializerByKey(serializers.ModelSerializer):
    product = serializers.CharField(source='product.product_name')
    class Meta:
        model = ReturnModel
        fields = ['product','problem','return_from','quantity']



class DamageSerializer(serializers.ModelSerializer):
    class Meta:
        model=DamageModel
        fields=['product','problem','quantity','added_by']
    
    def save(self,*args, **kwargs):
        instance = super().save(*args,**kwargs)
        print(self.data)

        product = ProductModel.objects.get(pk=self.data['product'])
        print(product,instance)
        # daminstance)

        instance.amount+=(product.purchase_price*int(self.data['quantity']))
        PLDModel.objects.create(profit=0,loss=0,damage=instance.amount)
        instance.save()



class DamageSerializerForUser(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.product_name')
    class Meta:
        model=DamageModel
        fields=['product_name','problem','amount','added_by']

    


