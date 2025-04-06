from django.shortcuts import render
from .models import ServiceCategory, Service

def home(request):
    """Главная страница с услугами и их категориями."""
    categories = ServiceCategory.objects.all()
    services = Service.objects.all()
    context = {
        'categories': categories,
        'services': services,
    }
    return render(request, 'main/index.html', context)
