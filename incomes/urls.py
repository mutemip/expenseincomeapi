from django.urls import path
from .views import IncomeListAPIView, IncomeDetailAPIView

urlpatterns = [
    path('', IncomeListAPIView.as_view(), name='Incomes'),
    path('<int:id>', IncomeDetailAPIView.as_view(), name='Income')
]