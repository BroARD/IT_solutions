from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.api_view import CarViewSet, CommentViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'cars', CarViewSet) #Регистрация ссылок для машин
router.register(r'cars/(?P<car_id>[^/.]+)/comments', CommentViewSet, basename='car-comments') #Регистрация ссылок для комментариев

urlpatterns = [
    path('admin/', admin.site.urls), #Ссылка на админку
    path("", include(router.urls)), #Ссылки на все ссылки router
]
