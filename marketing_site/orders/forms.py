from django import forms
from .models import Order
from main.models import Service

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['service', 'wishes', 'contact_method']

    # Дополнительные поля для подставления данных пользователя
    full_name = forms.CharField(
        label='ФИО',
        max_length=255,
        initial='',
        disabled=True  # Делается неактивным, чтобы пользователь не мог изменять
    )
    phone_number = forms.CharField(
        label='Номер телефона',
        max_length=20,
        initial='',
        disabled=True
    )
    email = forms.EmailField(
        label='Email',
        initial='',
        disabled=True
    )

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)

        # Если это новый заказ (т.е. ещё нет клиента), то подставляем данные из текущего пользователя
        if not self.instance.pk:  # Если объект ещё не сохранён
            user = kwargs.get('initial', {}).get('client', None) or kwargs.get('user', None)
            if user:
                self.fields['full_name'].initial = user.get_full_name()
                self.fields['phone_number'].initial = user.profile.phone_number if hasattr(user, 'profile') else ''
                self.fields['email'].initial = user.email
        else:
            # Автоматически заполняем данные из клиента, если они есть
            if self.instance.client:
                self.fields['full_name'].initial = self.instance.client.get_full_name()
                self.fields['phone_number'].initial = self.instance.client.phone_number if hasattr(self.instance.client, 'phone_number') else ''
                self.fields['email'].initial = self.instance.client.email