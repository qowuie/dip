from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('client', 'Клиент'),
        ('employee', 'Работник'),
        ('admin', 'Админ'),
    )

    middle_name = models.CharField("Отчество", max_length=150, blank=True)
    phone_number = models.CharField("Телефон", max_length=20)
    city = models.CharField("Город", max_length=100, blank=True)
    company = models.CharField("Компания", max_length=255, blank=True)

    # Роль
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')

    def __str__(self):
        return f"{self.get_full_name()} ({self.get_role_display()})"

    def get_full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}".strip()
