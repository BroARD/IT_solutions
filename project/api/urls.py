from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.api_view import CarViewSet, CommentViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'cars/(?P<car_id>[^/.]+)/comments', CommentViewSet, basename='car-comments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
]
