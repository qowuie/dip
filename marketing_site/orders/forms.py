from django import forms
from .models import Order
from ..main.models import Service

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['service', 'wishes', 'contact_method']

    # Дополнительные поля для подставления данных пользователя
    full_name = forms.CharField(
        label='ФИО',
        max_length=255,
        initial=lambda: '',  # Данные из User автоматически подтянутся в представлениях
        disabled=True  # Делается неактивным, чтобы пользователь не мог изменять
    )
    phone_number = forms.CharField(
        label='Номер телефона',
        max_length=20,
        initial=lambda: '',  # Аналогично
        disabled=True
    )
    email = forms.EmailField(
        label='Email',
        initial=lambda: '',  # Аналогично
        disabled=True
    )



    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            # Автоматически заполняем данные из пользователя, если они есть
            self.fields['full_name'].initial = self.instance.user.get_full_name()
            self.fields['phone_number'].initial = self.instance.user.profile.phone_number if hasattr(self.instance.user, 'profile') else ''
            self.fields['email'].initial = self.instance.user.email
