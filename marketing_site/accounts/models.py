# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('client', 'Клиент'),
        ('employee', 'Работник'),
        ('admin', 'Админ'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
