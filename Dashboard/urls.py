from django.urls import path,include
from .views import PDLView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
# router.register(r'pld',PLDModel)
urlpatterns = [
    # path('',include(router.urls)),
    path('pld/<get_date>/<type>/',PDLView.as_view())
]
