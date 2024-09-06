from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserRegisterForm((UserCreationForm)):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Имя пользователя', 'id':'username'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Электронная почта', 'id':'email'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Пароль', 'id':'password1'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Подтверждение пароля', 'id':'password2'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'id':'username', 'placeholder': 'Введите имя пользователя'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'id':'password', 'placeholder': 'Введите пароль'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')