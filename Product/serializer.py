from rest_framework import serializers
from .models import ProductModel,CategoryModel,BrandModel,UnitModel,PurchaseModel
from ExpansesAndPayments.models import PaymentModel

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductModel
        fields='__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=CategoryModel
        fields='__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model=BrandModel
        fields='__all__'

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model =UnitModel
        fields='__all__' 

class ProductSearchByNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields=['id','product_name','product_code','quantity','seals_price']


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=PurchaseModel
        fields='__all__'
    
    def save(self,*args, **kwargs):
        instance = super().save(*args, **kwargs)
        print(instance,instance.quantity,instance.purchase_price,instance.product)

        product = ProductModel.objects.get(pk=instance.product.id)
        product.quantity+=instance.quantity
        product.seals_price=instance.sales_price
        product.purchase_price=instance.purchase_price
        product.save()
        PaymentModel.objects.create(purchase = instance,company_name=instance.company_name,total_price=instance.total_price,cash=instance.cash,outstanding=instance.outstanding)

class PurchaseSerializerForView(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.product_name')

    class Meta:
        model = PurchaseModel
        fields = ['product_name','company_name','quantity']


class StockSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.product_name')
    current_price = serializers.CharField(source='product.seals_price')
    product_quantity = serializers.CharField(source='product.quantity')

    print(current_price,product_quantity)
    class Meta:
        model = PurchaseModel
        fields = ['product_name','company_name','date_time','product_quantity','current_price','purchase_price','sales_price']


        