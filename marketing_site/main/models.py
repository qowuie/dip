from django.db import models

class ServiceCategory(models.Model):
    """Категория услуги."""
    name = models.CharField("Название категории", max_length=255)
    description = models.TextField("Описание категории", blank=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    """Услуга, предлагаемая на сайте."""
    CATEGORY_CHOICES = [
        ('ai', 'AI'),
        ('performance_marketing', 'Performance Marketing'),
        ('seo', 'SEO'),
        ('analytics', 'Аналитика'),
        ('reputation_marketing', 'Репутационный маркетинг'),
        ('website_creation', 'Создание сайтов'),
        ('social_media_smm', 'Соц. сети и SMM'),
    ]

    name = models.CharField("Название услуги", max_length=255)
    description = models.TextField("Описание услуги")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name="services", verbose_name="Категория")
    category_type = models.CharField(max_length=255, choices=CATEGORY_CHOICES, default='ai', verbose_name="Тип категории")
    image = models.ImageField(upload_to="services/", null=True, blank=True, verbose_name="Изображение")

    def __str__(self):
        return self.name
