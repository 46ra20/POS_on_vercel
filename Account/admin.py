from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from django.http import HttpRequest
from django.http.response import HttpResponse
# from models import RegistrationModel
from .models import RegistrationModel
from datetime import datetime


# Register your models here.
class AdminUpdate(admin.ModelAdmin):

    def change_view(self, request: HttpRequest, object_id: str) -> HttpResponse:
        us = RegistrationModel.objects.get(id=object_id)
        if us.type=='Manager':
            us.user.is_superuser=True
            us.user.save()
        elif us.type=='Staf':
            us.user.is_staff=True
        elif us.type=='General':
            us.user.is_staff=False
            us.user.is_superuser=False
        print(datetime.now(),request.user.id, object_id,us.type)
        return super().change_view(request, object_id)
    def save(self,object):
        print(object)
    

admin.site.register(RegistrationModel,AdminUpdate)