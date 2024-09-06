from django import forms
from .models import Car, Comment

#Форма создания нового автомобиля
class CarForm(forms.ModelForm):
    make = forms.CharField(widget=forms.TextInput(attrs={
        'id': "make", 'placeholder': "Марка"
    }))
    model = forms.CharField(widget=forms.TextInput(attrs={
        'id': "model", 'placeholder': "Модель"
    }))
    year = forms.IntegerField(widget=forms.NumberInput(attrs={
        'id': "year", 'placeholder': "Год выпуска"
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'id': "description", 'placeholder': "Описание", 'rows':4
    }))

    class Meta:
        model = Car
        fields = ('make', 'model', 'year', 'description')

#Форма написания нового комментария
class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Оставьте ваш комментарий...', 'rows':'4'
    }))

    class Meta:
        model = Comment
        fields = ('content', )
