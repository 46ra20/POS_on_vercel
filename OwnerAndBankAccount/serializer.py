from .models import OwnerModel,BankAccountModel
from rest_framework import serializers

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerModel
        fields = '__all__'

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccountModel
        fields = '__all__'