from SalesProduct.models import SalesModel
from rest_framework import serializers

class PromotionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesModel
        fields=['customer_name','mobile_no','address','city','country']