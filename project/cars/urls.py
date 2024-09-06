from django.urls import path
from .views import CarsListView, CarView, edit_car, delete_car

app_name = 'cars'

urlpatterns = [
    path('', CarsListView.as_view(), name='cars'),
    path('<int:car_id>/', CarView.as_view(), name='car'),
    path('<int:car_id>/edit/', edit_car, name='car_edit'),
    path('delete_car/<int:car_id>/', delete_car, name='delete_car')
]
