# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    # Поля для имени, фамилии и отчества
    first_name = forms.CharField(max_length=150, label="Имя", required=True)
    last_name = forms.CharField(max_length=150, label="Фамилия", required=True)
    middle_name = forms.CharField(max_length=150, label="Отчество", required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'middle_name', 'email', 'password1', 'password2', 'role')  # Изменен порядок полей

    # Дополнительно, если нужно, можно настроить валидацию или другие действия
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Опционально, можно настроить какие-то кастомные атрибуты для полей, например, placeholder
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Введите ваше имя'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Введите вашу фамилию'})
        self.fields['middle_name'].widget.attrs.update({'placeholder': 'Введите ваше отчество'})


class CustomAuthenticationForm(AuthenticationForm):
    pass
