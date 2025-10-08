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
from django.http import JsonResponse

def welcome_view(request):
    return JsonResponse({"message": "Welcome to Narok Revenue System "})
# Admin Dashboard
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.db.models import Sum
from .models import Payment, RevenueSource, CountyZone
from django.utils.timezone import now, timedelta

class AdminDashboardView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        today = now().date()
        week_ago = today - timedelta(days=7)

        zone_summary = CountyZone.objects.annotate(
            total_revenue=Sum('payment__amount')
        ).values('name', 'total_revenue')

        source_summary = RevenueSource.objects.annotate(
            total_revenue=Sum('payment__amount')
        ).values('name', 'total_revenue')

        daily_total = Payment.objects.filter(date=today).aggregate(Sum('amount'))['amount__sum'] or 0
        weekly_total = Payment.objects.filter(date__gte=week_ago).aggregate(Sum('amount'))['amount__sum'] or 0

        return Response({
            'zone_summary': list(zone_summary),
            'source_summary': list(source_summary),
            'daily_total': daily_total,
            'weekly_total': weekly_total,
        })