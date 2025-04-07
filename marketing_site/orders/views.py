from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order
from django.contrib.auth.decorators import login_required


@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.client = request.user  # Присваиваем клиента
            order.save()
            return redirect('order_success')
    else:
        form = OrderForm(initial={'client': request.user})  # Передаем пользователя в форму через initial
    return render(request, 'orders/create_order.html', {'form': form})


@login_required
def order_success(request):
    return render(request, 'orders/order_success.html')
