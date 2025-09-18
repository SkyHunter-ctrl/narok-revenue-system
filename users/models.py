from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('PAYER', 'Revenue Payer'),
        ('COLLECTOR', 'Revenue Collector'),
        ('ADMIN', 'County Admin'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',
        blank=True
    )

    zone = models.ForeignKey(
        'revenue.CountyZone',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

