from django.contrib import admin
from .models import Car, Comment

# Register your models here.
admin.site.register(Car) #Доступ к машинам в админке
admin.site.register(Comment) #Доступ к комментариям в админке
