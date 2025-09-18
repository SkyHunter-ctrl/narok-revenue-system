from rest_framework import serializers
from .models import RevenueSource, Payment

class RevenueSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueSource
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        