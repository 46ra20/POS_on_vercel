from django.db import models
from django.contrib.auth.models import User
from Product.models import ProductModel

# Create your models here.


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