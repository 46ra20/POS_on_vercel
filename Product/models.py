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
    quantity =models.IntegerField(default=0)
    purchase_price =models.DecimalField(max_digits=12,decimal_places=2,default=0)
    seals_price =models.DecimalField(max_digits=12,decimal_places=2,default=0)
    date = models.DateField(auto_now_add=True)

    category = models.ManyToManyField(CategoryModel)
    brand = models.ForeignKey(BrandModel,on_delete=models.CASCADE,default='')
    added_by = models.ForeignKey(User,on_delete=models.CASCADE,default='')

    def __str__(self) -> str:
        return f'{self.product_name} by {self.added_by.first_name} {self.added_by.last_name}'
    

class PurchaseModel(models.Model):
    product = models.ForeignKey(ProductModel,on_delete=models.SET_NULL,null=True,default='')
    company_name=models.CharField(max_length=150,default='')
    quantity = models.IntegerField(default=0)
    purchase_price = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    sales_price = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    total_price = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    cash = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    outstanding = models.DecimalField(max_digits=12, decimal_places=2,default=0)

    date_time = models.DateField(auto_now_add=True)

    purchase_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,default='')

    def __str__(self) -> str:
        return f'{self.product.product_name} added by {self.purchase_by.first_name} {self.purchase_by.last_name}'