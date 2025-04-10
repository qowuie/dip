from django import forms
from .models import Order
from main.models import Service


class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(OrderForm, self).__init__(*args, **kwargs)

        if self.user:
            self.fields['full_name'].initial = self.user.get_full_name()
            self.fields['phone_number'].initial = self.user.phone_number
            self.fields['email'].initial = self.user.email
        elif self.instance and self.instance.client:
            self.fields['full_name'].initial = self.instance.client.get_full_name()
            self.fields['phone_number'].initial = self.instance.client.phone_number
            self.fields['email'].initial = self.instance.client.email

    class Meta:
        model = Order
        fields = ['service', 'wishes', 'contact_method']

    full_name = forms.CharField(label='ФИО', max_length=255, disabled=True)
    phone_number = forms.CharField(label='Номер телефона', max_length=20, disabled=True)
    email = forms.EmailField(label='Email', disabled=True)