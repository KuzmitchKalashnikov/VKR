from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-green-500',
        'placeholder': 'Имя пользователя'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-green-500',
        'placeholder': 'Пароль'
    }))


class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-green-500',
        'placeholder': 'Имя пользователя'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-green-500',
        'placeholder': 'Email'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-green-500',
        'placeholder': 'Пароль'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-green-500',
        'placeholder': 'Подтверждение пароля'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
