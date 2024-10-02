from django.db import models
from Product.models import PurchaseModel
from django.contrib.auth.models import User
# Create your models here.
class PaymentModel(models.Model):
    company_name = models.CharField(max_length=150,default='')
    total_price = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    cash = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    outstanding = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    date=models.DateField(auto_now_add=True)

    purchase = models.ForeignKey(PurchaseModel, on_delete=models.SET_NULL,null=True,default='')
    def __str__(self) -> str:
        return f'{self.purchase.product.product_name} from {self.purchase.company_name}'
    
class ExpensesModel(models.Model):
    for_what = models.CharField(max_length=100,default='')
    amount = models.DecimalField(max_digits=12,decimal_places=2,default=0)
    cash = models.DecimalField(max_digits=12,decimal_places=2,default=0)
    outstanding = models.DecimalField(max_digits=12,decimal_places=2,default=0)
    date = models.DateField( auto_now_add=True)

    expense_by = models.ForeignKey(User,on_delete=models.SET_NULL,default='',null=True)

    def __str__(self) -> str:
        return f'{self.for_what} expense by {self.expense_by.first_name} {self.expense_by.last_name}'