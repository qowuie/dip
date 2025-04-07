# main/models.py

from django.db import models


class ServiceCategory(models.Model):
    name = models.CharField("Название категории", max_length=255)
    description = models.TextField("Описание категории", blank=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField("Название услуги", max_length=255)
    description = models.TextField("Описание услуги")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.CASCADE,
        related_name="services",
        verbose_name="Категория"
    )
    image = models.ImageField(upload_to="services/", null=True, blank=True, verbose_name="Изображение")

    def __str__(self):
        return self.name
