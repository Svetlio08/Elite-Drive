from django.urls import reverse_lazy
from django.views import generic as g

from .models import Brand, Feature
import catalog.forms as f

class BrandListView(g.ListView):
    model = Brand
    template_name = "catalog/brand_list.html"
    context_object_name = "brands"
    ordering = ["name"]


class BrandCreateView(g.CreateView):
    model = Brand
    form_class = f.BrandForm
    template_name = "catalog/brand_form.html"
    success_url = reverse_lazy("brand-list")


class BrandEditView(g.UpdateView):
    model = Brand
    form_class = f.BrandForm
    template_name = "catalog/brand_form.html"
    success_url = reverse_lazy("brand-list")


class BrandDeleteView(g.DeleteView):
    model = Brand
    template_name = "catalog/brand_confirm_delete.html"
    success_url = reverse_lazy("brand-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = f.BrandDeleteForm(instance=self.object)
        return context


class FeatureListView(g.ListView):
    model = Feature
    template_name = "catalog/feature_list.html"
    context_object_name = "features"
    ordering = ["name"]


class FeatureCreateView(g.CreateView):
    model = Feature
    form_class = f.FeatureForm
    template_name = "catalog/feature_form.html"
    success_url = reverse_lazy("feature-list")


class FeatureEditView(g.UpdateView):
    model = Feature
    form_class = f.FeatureForm
    template_name = "catalog/feature_form.html"
    success_url = reverse_lazy("feature-list")


class FeatureDeleteView(g.DeleteView):
    model = Feature
    template_name = "catalog/feature_confirm_delete.html"
    success_url = reverse_lazy("feature-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = f.FeatureDeleteForm(instance=self.object)
        return context