from django.shortcuts import render
from .serializer import RegistrationSerializers,UserLoginSerializer
from .models import RegistrationModel,User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
from django.contrib.auth.tokens import default_token_generator
# Create your views here.

class RegistrationView(APIView):
    serializer_class = RegistrationSerializers

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = default_token_generator.make_token(user[0])
            print(user,token)
            return Response({'message':'Account created successfully'})
        
        return Response(serializer.errors)
        


class LoginView(APIView):
    serializer_class = UserLoginSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            print(username,password)
            auth = authenticate(request=request,username=username,password=password)
            if(auth):
                user = login(request=request,user=auth)
                return Response({'message':'Login successfully','type':"success",'user':user})

            elif User.objects.filter(username=username):
                return Response({'password':"Please enter correct password",'type':"warning"})
            else:
                return Response({'username':"User doesn't exist.",'type':"danger"})
        # if(serializer.is_valid()):
        #     username=serializer.validated_data['username']
        #     password=serializer.validated_data['password']
        #     auth = authenticate(request=request,username=username,password=password)

        #     print(auth)
        #     if User.objects.filter(username=username):
        #         return Response({'message':"Please enter correct password",'type':"warning"})
        #     login(request=request,user=auth)
        #     if auth:
        #         return Response({'message':'Login successfully','type':"success"})
        #     return Response({'message':"Sorry, No user with this username.",'type':"danger"})
        return Response(serializer.errors)
    
class LogoutView(APIView):
    def get(self,request):
        lu=logout(request=request)
        print(lu)
        if not lu:
            return Response({'message':"Logout successfully","type":"success"})
        return Response({'message':"Something wrong please try agin","type":"danger"})
        
