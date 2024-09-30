from django.db import models
from SalesProduct.models import SalesModel
# Create your models here.
class PLDModel(models.Model):
    profit = models.DecimalField(max_digits=20,decimal_places=2)
    loss = models.DecimalField(max_digits=20,decimal_places=2)
    damage = models.DecimalField(max_digits=20,decimal_places=2)
    date = models.DateField(auto_now_add=True)

    # sales = models.ForeignKey(SalesModel,on_delete=models.SET_NULL,null=True,blank=False,default='')

    def __str__(self) -> str:
        return f'{self.sales.customer_name} {self.sales.address}'

