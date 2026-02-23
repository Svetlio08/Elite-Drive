from django.urls import reverse_lazy
from django.views import generic as g

from .models import Car
from cars import forms as f


class CarListView(g.ListView):
    model = Car
    template_name = "cars/car_list.html"
    context_object_name = "cars"
    paginate_by = 9

class CarDetailView(g.DetailView):
    model = Car
    template_name = "cars/car_detail.html"
    context_object_name = "car"

class CarCreateView(g.CreateView):
    model = Car
    form_class = f.CarCreateForm
    template_name = "cars/car_form.html"
    success_url = reverse_lazy("car-list")


class CarEditView(g.UpdateView):
    model = Car
    form_class = f.CarEditForm
    template_name = "cars/car_form.html"
    success_url = reverse_lazy("car-list")


class CarDeleteView(g.DeleteView):
    model = Car
    template_name = "cars/car_confirm_delete.html"
    success_url = reverse_lazy("car-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = f.CarDeleteForm(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)