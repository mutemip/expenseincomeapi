from rest_framework import serializers
from .models import Expense


class ExpenseListAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'date', 'description', 'amount', 'category']

class ExpenseDetailAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'date', 'description', 'amount', 'category']
