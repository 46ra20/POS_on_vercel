from django.urls import path,include
from rest_framework import routers
from .views import RegistrationView,LoginView,LogoutView

router = routers.DefaultRouter()
# router.register(r'registration',RegistrationView)

urlpatterns = [
    path('registration/',RegistrationView.as_view(),name='registration'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout')
]
