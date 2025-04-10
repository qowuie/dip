# Generated by Django 4.2 on 2025-04-07 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wishes', models.TextField(blank=True, verbose_name='Дополнительные пожелания')),
                ('contact_method', models.CharField(max_length=255, verbose_name='Предпочитаемый способ связи')),
                ('status', models.CharField(choices=[('created', 'Создан'), ('in_progress', 'В работе'), ('completed', 'Выполнен')], default='created', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_orders', to=settings.AUTH_USER_MODEL, verbose_name='Клиент')),
                ('executor', models.ForeignKey(blank=True, limit_choices_to={'role': 'employee'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='executor_orders', to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.service', verbose_name='Услуга')),
            ],
        ),
    ]
