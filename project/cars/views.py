from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from .models import Car, Comment
from .forms import CarForm, CommentForm
from django.urls import reverse_lazy

from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse

#Главная страница
class MainPageView(TemplateView):
    template_name = 'cars/main_page.html'

#Список всех автомобилей с формай для добавления нового, при условии что вы авторизованы
class CarsListView(CreateView):
    model = Car
    template_name = 'cars/cars_list.html'
    form_class = CarForm
    success_url = reverse_lazy('cars:cars')

    def get_context_data(self, **kwargs):
        ctx = super(CarsListView, self).get_context_data()
        ctx['cars'] = Car.objects.all()

        return ctx

    def form_valid(self, form):
        form.instance.owner = self.request.user

        return super(CarsListView, self).form_valid(form)


#Контроллер просмотра профиля автомобиля и комментариев к нему.
class CarView(CreateView):
    model = Car
    template_name = 'cars/car.html'
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        car = Car.objects.get(id=self.kwargs['car_id'])
        form.instance.car = car

        return super(CarView, self).form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(CarView, self).get_context_data()
        ctx['car'] = Car.objects.get(id=self.kwargs['car_id'])
        ctx['comments'] = Comment.objects.filter(car_id=self.kwargs['car_id'])

        return ctx

    def get_success_url(self):
        return reverse_lazy('cars:car', kwargs={'car_id': self.kwargs.get('car_id')})

#Редактирование автомобиля, если вы его владелец
@login_required
def edit_car(request, car_id):
    car = Car.objects.get(id=car_id)

    if car.owner != request.user:
        return render(request, 'cars/permission_denied.html')

    if request.method == 'POST':
        car.make = request.POST['make']
        car.model = request.POST['model']
        car.year = request.POST['year']
        car.description = request.POST['description']
        car.save()
        return HttpResponseRedirect(reverse('cars:cars'))

    return render(request, 'cars/car_edit.html', {'car': car})

#Удаления автомобиля, если вы его владелец
@login_required
def delete_car(request, car_id):
    if request.user == Car.objects.get(id=car_id).owner:
        Car.objects.get(id=car_id).delete()
    return HttpResponseRedirect(reverse('cars:cars'))
