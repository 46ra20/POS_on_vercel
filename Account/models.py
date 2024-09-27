from django.db import models
from django.contrib.auth.models import User

# Create your models here.
ACCOUNT_TYPE=(
    ('General','General'),
    ('Staf','Staf'),
    ('Manager','Manager')
)

class RegistrationModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.CharField(max_length=100,default='')
    date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=100,choices=ACCOUNT_TYPE,blank=False)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'
    
class UserLoginModel(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
