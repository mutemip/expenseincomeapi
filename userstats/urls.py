from django.urls import path
from .views import ExpenseSummaryAPIView, IncomeSummaryAPIView

urlpatterns = [
    path('expense_category_summery', ExpenseSummaryAPIView.as_view(), name='expense-category-summery'),
    path('income_source_data', IncomeSummaryAPIView.as_view(), name='income-source-data')
]
