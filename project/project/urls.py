from django.contrib import admin
from django.urls import path, include
from users.views import UserRegistrationView, UserLoginView
from django.contrib.auth.views import LogoutView
from cars.views import MainPageView



urlpatterns = [
    path('admin/', admin.site.urls), #Админка
    path("api/", include('api.urls')), #DRF
    path('cars/', include('cars.urls')), #Доступ к списку машин
    path('', MainPageView.as_view(), name='main_page'), #Главная страница
    path('login/', UserLoginView.as_view(), name='login'), #Логин пользователя
    path('register/', UserRegistrationView.as_view(), name='register'), #Регистрация пользователя
    path('logout/', LogoutView.as_view(), name='logout') #Выход из системы
]
