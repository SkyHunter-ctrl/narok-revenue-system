from django.shortcuts import render
from rest_framework import viewsets
from .models import RevenueSource, Payment
from .serializers import RevenueSourceSerializer, PaymentSerializer
from rest_framework.permissions import IsAuthenticated

class RevenueSourceViewSet(viewsets.ModelViewSet):
    queryset = RevenueSource.objects.all()
    serializer_class = RevenueSourceSerializer
    permission_classes = [IsAuthenticated]

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

# Create your views here.
