from django.db import models
from ..accounts.models import CustomUser  # Импортируем CustomUser
from ..main.models import Service  # предполагается, что услуги у тебя в приложении main

class Order(models.Model):
    STATUS_CHOICES = [
        ('created', 'Создан'),
        ('in_progress', 'В работе'),
        ('completed', 'Выполнен'),
    ]

    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Клиент")

    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, verbose_name="Услуга")
    wishes = models.TextField("Дополнительные пожелания", blank=True)
    contact_method = models.CharField("Предпочитаемый способ связи", max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='created')
    created_at = models.DateTimeField(auto_now_add=True)
    executor = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name="assigned_orders", verbose_name="Исполнитель",
                                 limit_choices_to={'role': 'employee'})  # Только сотрудник

    def __str__(self):
        return f"{self.client.username} - {self.service}"

    def get_full_name(self):
        return self.client.get_full_name()

    def get_email(self):
        return self.client.email

    def get_phone_number(self):

        return self.client.profile.phone_number if hasattr(self.user, 'profile') else 'Не указан'
