from django.db import models
from django.contrib.auth.models import User
from Product.models import ProductModel

# Create your models here.

WHERE_FROM = (
    ('CUSTOMER','Customer'),
    ('OURSELF','Ourself'),

)

class SalesModel(models.Model):
    customer_name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=20,null=True,blank=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30,null=True,blank=True)
    country = models.CharField(max_length=30,null=True,blank=True)
    total_price = models.DecimalField(max_digits=12,decimal_places=2,default=0)
    cash = models.DecimalField(max_digits=12,decimal_places=2,default=0)
    outstanding = models.DecimalField(max_digits=12,decimal_places=2,default=0)
    sales_item = models.ManyToManyField(ProductModel)
    sales_quantity=models.CharField(max_length=300)
    # sales_item=models.ExpressionList()

    seller = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.customer_name} seller {self.seller.first_name} {self.seller.last_name}'
    

class ReturnModel(models.Model):
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE,default='')
    problem=models.CharField(max_length=200)
    return_from = models.CharField(choices=WHERE_FROM,max_length=20)
    quantity= models.IntegerField()

    return_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self) -> str:
        return f'{self.product.product_name} - {self.return_by.first_name}'
    

class DamageModel(models.Model):
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE,default='')
    problem = models.CharField(max_length=200)
    quantity = models.IntegerField()
    amount = models.DecimalField(max_digits=12,default=0,decimal_places=2)

    added_by = models.ForeignKey(User,on_delete=models.SET_NULL,default='',null=True)


    def __str__(self) -> str:
        return f'Damage {self.product.product_name}'
    