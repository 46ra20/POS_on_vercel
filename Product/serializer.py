from rest_framework import serializers
from .models import ProductModel,CategoryModel,BrandModel,UnitModel

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