from django.db import models
from Account.models import User

# Create your models here.
class CategoryModel(models.Model):
    category=models.CharField(max_length=30)
    slug=models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.category
    
class BrandModel(models.Model):
    brand=models.CharField(max_length=30)
    slug = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.brand
    
class UnitModel(models.Model):
    unit=models.CharField(max_length=20)
    slug=models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.unit
    

class ProductModel(models.Model):
    product_name = models.CharField(max_length=100)
    product_code =models.CharField(max_length=30)
    quantity =models.IntegerField()
    purchase_price =models.IntegerField()
    seals_price =models.IntegerField()
    date = models.DateField(auto_now_add=True)

    category = models.ManyToManyField(CategoryModel)
    brand = models.ForeignKey(BrandModel,on_delete=models.CASCADE)
    added_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.product_name} by {self.added_by.first_name} {self.added_by.first_name}'