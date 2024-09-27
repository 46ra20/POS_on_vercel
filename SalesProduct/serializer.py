from rest_framework import serializers
from .models import SalesModel,ProductModel

class SalesSerializers(serializers.ModelSerializer):
    class Meta:
        model = SalesModel
        fields = '__all__'

    def save(self):
        print(self.data)
        quantity = self.data['sales_quantity'].split(',')
        items = self.data['sales_item']
        i=0
        for item in items:
            product = ProductModel.objects.get(id=item)
            product.quantity-=int(quantity[i])
            i+=1
            product.save()


