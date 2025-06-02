# orders/models.py

from django.db import models
from accounts.models import CustomUser
from main.models import Service


class Employee(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    id_1c = models.CharField(max_length=9, unique=True)  # ID из 1С

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Order(models.Model):
    STATUS_CHOICES = [
        ('created', 'Создан'),
        ('in_progress', 'В работе'),
        ('completed', 'Выполнен'),
    ]

    client = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name="Клиент",
        related_name="client_orders"
    )

    executor = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)

    service = models.ForeignKey(
        Service,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Услуга"
    )

    wishes = models.TextField("Дополнительные пожелания", blank=True)
    contact_method = models.CharField("Предпочитаемый способ связи", max_length=255)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='created'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Заказ {self.id} от {self.client.username}"

    def get_full_name(self):
        return self.client.get_full_name()

    def get_email(self):
        return self.client.email

    def get_phone_number(self):
        return self.client.phone_number if hasattr(self.client, 'phone_number') else 'Не указан'


