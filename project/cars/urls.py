from django.urls import path
from .views import CarsListView, CarView, edit_car, delete_car

app_name = 'cars'

urlpatterns = [
    path('', CarsListView.as_view(), name='cars'), # Список автомобилей
    path('<int:car_id>/', CarView.as_view(), name='car'), #Характеристики автомобиля и комментарии по ID
    path('<int:car_id>/edit/', edit_car, name='car_edit'), #Редактирование параметров автомобиля,
                                                            # если владелец==пользователь
    path('delete_car/<int:car_id>/', delete_car, name='delete_car') #Кнопка удаления автомобиля
]
