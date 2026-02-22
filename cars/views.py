from django.views import generic as g

from .models import Car

class CarListView(g.ListView):
    model = Car
    template_name = 'cars/car_list.html'

class CarDetailView(g.DetailView):
    model = Car
    template_name = 'cars/car_detail.html'

class CarCreateView(g.CreateView):
    model = Car
    template_name = 'cars/car_form.html'

class CarEditView(g.UpdateView):
    model = Car
    template_name = 'cars/car_form.html'

class CarDeleteView(g.DeleteView):
    model = Car
    template_name = 'cars/car_confirm_delete.html'