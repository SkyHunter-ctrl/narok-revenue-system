from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RevenueSourceViewSet, PaymentViewSet

router = DefaultRouter()
router.register(r'sources', RevenueSourceViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]