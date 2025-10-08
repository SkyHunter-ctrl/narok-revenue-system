from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RevenueSourceViewSet, PaymentViewSet, welcome_view, AdminDashboardView


router = DefaultRouter()
router.register(r'sources', RevenueSourceViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('', welcome_view),  # ✅ Handles root of /api/
    path('admin/dashboard/', AdminDashboardView.as_view(), name='admin-dashboard'),
    path('', include(router.urls)),
    

]
