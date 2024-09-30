from django.contrib import admin
from .models import SalesModel,ReturnModel,DamageModel
# Register your models here.


admin.site.register(SalesModel)
admin.site.register(ReturnModel)
admin.site.register(DamageModel)