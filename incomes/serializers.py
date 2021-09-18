from rest_framework import serializers
from .models import Income


class IncomeListAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['date', 'description', 'amount', 'source']

class IncomeDetailAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = ['id','date', 'description', 'amount', 'source']
