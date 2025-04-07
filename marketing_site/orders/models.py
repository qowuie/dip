# orders/models.py

from django.db import models
from ..accounts.models import CustomUser
from ..main.models import Service


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

    executor = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="executor_orders",
        verbose_name="Исполнитель",
        limit_choices_to={'role': 'employee'}
    )

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
