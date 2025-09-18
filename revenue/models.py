from django.db import models
from django.contrib.auth.models import User
from django.db import models

class RevenueSource(models.Model):
    CATEGORY_CHOICES = [
        ('BUSINESS_LICENSE', 'Business License'),
        ('PARKING_FEE', 'Parking Fee'),
        ('TOWNSHIP', 'Township'),
        ('PSV_FEES', 'PSV Fees'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"
class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    payer_name = models.CharField(max_length=100)
    source = models.ForeignKey(RevenueSource, on_delete=models.CASCADE)
    collector = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.payer_name} - {self.amount} on {self.date}"
class CountyZone(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


