from django.shortcuts import render
from django.views.generic import TemplateView

from cars.models import Car
from catalog.models import Brand
from showroom.models import Collection


class HomeView(TemplateView):
    template_name = "common/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["cars_count"] = Car.objects.count()
        context["brands_count"] = Brand.objects.count()
        context["collections_count"] = Collection.objects.count()

        context["latest_cars"] = Car.objects.select_related("brand").order_by("-created_at")[:6]

        context["featured_collections"] = (
            Collection.objects
            .prefetch_related("cars")
            .filter(is_featured=True)
            .order_by("-created_at")[:6]
        )

        return context


def custom_404(request, exception):
    return render(request, "common/404.html", status=404)