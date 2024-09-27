from rest_framework import serializers
from .models import RegistrationModel,User,UserLoginModel
from .models import ACCOUNT_TYPE

class RegistrationSerializers(serializers.ModelSerializer):
    image = serializers.ImageField()
    type = serializers.ChoiceField(choices=ACCOUNT_TYPE)
    confirm_password=serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','image','type','password','confirm_password']
    
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        image = self.validated_data['image']
        type = self.validated_data['type']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if(User.objects.filter(username=username)):
            return serializers.ValidationError({'username':'Username already exist.'})
        if(User.objects.filter(email=email)):
            raise serializers.ValidationError({'email':'Email already exist.'})
        if(password != confirm_password):
            raise serializers.ValidationError({'password':"Password doesn't match"})
        
        account = User(username=username,first_name=first_name,last_name=last_name,email=email)
        registration_model = RegistrationModel(user=account,image=image,type=type)
        if(type=='Manager'):
            account.is_superuser=True
        if(type=='Staf'):
            account.is_staff=True
        account.set_password(password)
        account.save()
        registration_model.save()

        return account,registration_model

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    class Meta:
        model = User
        