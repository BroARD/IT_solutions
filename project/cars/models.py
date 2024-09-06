from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Модель автомобиля
class Car(models.Model):
    make = models.CharField(max_length=16, verbose_name='make')
    model = models.CharField(max_length=16, verbose_name='model')
    year = models.SmallIntegerField(verbose_name='year')
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(to=User, verbose_name='owner', on_delete=models.CASCADE)

    def __str__(self):
        return f'Owner: {self.owner}, {self.make} {self.model}'

#Модель комментария
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    car = models.ForeignKey(to=Car, verbose_name='car', on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, verbose_name='author', on_delete=models.CASCADE)
