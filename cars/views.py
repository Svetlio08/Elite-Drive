from django.urls import reverse_lazy
from django.views import generic as g

from .models import Car
from cars import forms as f
from catalog.models import Brand, Feature


class CarListView(g.ListView):
    model = Car
    template_name = "cars/car_list.html"
    context_object_name = "cars"
    paginate_by = 9

    def get_queryset(self):
        qs = (
            Car.objects
            .select_related("brand")
            .prefetch_related("features")
        )

        brand_id = self.request.GET.get("brand")
        fuel = self.request.GET.get("fuel")
        trans = self.request.GET.get("trans")
        feature_id = self.request.GET.get("feature")
        q = self.request.GET.get("q")
        min_price = self.request.GET.get("min_price")
        max_price = self.request.GET.get("max_price")
        year_from = self.request.GET.get("year_from")
        year_to = self.request.GET.get("year_to")
        sort = self.request.GET.get("sort", "newest")

        if q:
            qs = qs.filter(
                Q(model_name__icontains=q) |
                Q(brand__name__icontains=q)
            )

        if brand_id:
            qs = qs.filter(brand_id=brand_id)

        if fuel:
            qs = qs.filter(fuel_type=fuel)

        if trans:
            qs = qs.filter(transmission=trans)

        if feature_id:
            qs = qs.filter(features__id=feature_id)

        if min_price:
            try:
                qs = qs.filter(price__gte=min_price)
            except ValueError:
                pass

        if max_price:
            try:
                qs = qs.filter(price__lte=max_price)
            except ValueError:
                pass

        if year_from:
            try:
                qs = qs.filter(year__gte=int(year_from))
            except ValueError:
                pass

        if year_to:
            try:
                qs = qs.filter(year__lte=int(year_to))
            except ValueError:
                pass

        qs = qs.distinct()

        sort_map = {
            "newest": "-created_at",
            "price_asc": "price",
            "price_desc": "-price",
            "year_desc": "-year",
            "hp_desc": "-horsepower",
        }
        qs = qs.order_by(sort_map.get(sort, "-created_at"))

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brands"] = Brand.objects.order_by("name")
        context["features_all"] = Feature.objects.order_by("name")
        context["fuel_choices"] = Car.FuelType.choices
        context["trans_choices"] = Car.TransmissionType.choices
        context["current"] = {
            "brand": self.request.GET.get("brand", ""),
            "fuel": self.request.GET.get("fuel", ""),
            "trans": self.request.GET.get("trans", ""),
            "feature": self.request.GET.get("feature", ""),
            "q": self.request.GET.get("q", ""),
            "min_price": self.request.GET.get("min_price", ""),
            "max_price": self.request.GET.get("max_price", ""),
            "year_from": self.request.GET.get("year_from", ""),
            "year_to": self.request.GET.get("year_to", ""),
            "sort": self.request.GET.get("sort", "newest"),
        }
        return context

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