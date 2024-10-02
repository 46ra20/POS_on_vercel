from django.contrib import admin
from .models import PaymentModel,ExpensesModel
# Register your models here.

admin.site.register(PaymentModel)
admin.site.register(ExpensesModel)
