from rest_framework.urls import path
from .views import PaymentView,PaymentUpdateView,ExpanseView
urlpatterns = [
    path('payment/<key>/',PaymentView.as_view({'get':'list'})),
    path('payment_update/<int:pk>/',PaymentUpdateView.as_view()),
    path('expanse/',ExpanseView.as_view({'get':'list'})),
    path('expanse_add/',ExpanseView.as_view({'post':'create'})),
]
