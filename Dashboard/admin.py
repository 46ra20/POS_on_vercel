from django.contrib import admin
from .models import PLDModel
# Register your models here.
class Display(admin.ModelAdmin):
    list_display=('customerName','address','profit','loss','damage')
    def customerName(self,obj):
        return obj.sales.customer_name
    def address(self,obj):
        return obj.sales.address

admin.site.register(PLDModel,Display)
