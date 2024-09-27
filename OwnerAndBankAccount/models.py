from django.db import models

# Create your models here.


class OwnerModel(models.Model):
    name=models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    school = models.CharField(max_length=100,blank=True,null=True)
    collage = models.CharField(max_length=100,blank=True,null=True)
    university = models.CharField(max_length=100,blank=True,null=True)
    mobile = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name
    
class BankAccountModel(models.Model):
    bank_name = models.CharField(max_length=100)
    account_name= models.CharField(max_length=80)
    account_no = models.IntegerField()
    mobile = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.account_name
