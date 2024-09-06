from django.contrib import admin
from django.urls import path, include
from users.views import UserRegistrationView, UserLoginView
from django.contrib.auth.views import LogoutView
from cars.views import MainPageView



urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include('api.urls')),
    path('cars/', include('cars.urls')),
    path('', MainPageView.as_view(), name='main_page'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout')
]
