from rest_framework.urls import path
from .views import PromotionalView
urlpatterns = [
    path('promotional_list/',PromotionalView.as_view({'get':'list'}))
]
