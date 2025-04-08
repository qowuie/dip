# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, label="Имя", required=True)
    last_name = forms.CharField(max_length=150, label="Фамилия", required=True)
    middle_name = forms.CharField(max_length=150, label="Отчество", required=False)
    phone_number = forms.CharField(max_length=20, label="Телефон", required=True)

    class Meta:
        model = CustomUser
        fields = (
            'username', 'first_name', 'last_name', 'middle_name',
            'phone_number', 'email', 'password1', 'password2'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Введите ваше имя'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Введите вашу фамилию'})
        self.fields['middle_name'].widget.attrs.update({'placeholder': 'Введите ваше отчество'})
        self.fields['phone_number'].widget.attrs.update({
            'placeholder': '+7 (___) ___-__-__',
            'id': 'phone-input'
        })


class CustomAuthenticationForm(AuthenticationForm):
    pass
