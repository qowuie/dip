from django.shortcuts import render
from .models import ServiceCategory, Service
from utils.jwt_token import generate_matching_key_token


def home(request):
    """Главная страница с услугами и их категориями."""
    categories = ServiceCategory.objects.all()
    services = Service.objects.all()

    # ✅ Генерация токена, если пользователь вошёл
    matching_key_token = None
    if request.user.is_authenticated:
        matching_key_token = generate_matching_key_token(str(request.user.id))

    context = {
        'categories': categories,
        'services': services,
        'matching_key_token': matching_key_token
    }
    return render(request, 'main/index.html', context)
