from django.contrib import admin
from .models import OwnerModel,BankAccountModel
# Register your models here.

admin.site.register(OwnerModel)
admin.site.register(BankAccountModel)