from django.views import generic as g

from .models import Brand, Feature


class BrandListView(g.ListView):
    model = Brand
    template_name = 'catalog/brand_list.html'

class BrandCreateView(g.CreateView):
    model = Brand
    template_name = 'catalog/brand_form.html'

class BrandEditView(g.UpdateView):
    model = Brand
    template_name = 'catalog/brand_form.html'

class BrandDeleteView(g.DeleteView):
    model = Brand
    template_name = 'catalog/brand_confirm_delete.html'

class FeatureListView(g.ListView):
    model = Feature
    template_name = 'catalog/feature_list.html'

class FeatureCreateView(g.CreateView):
    model = Feature
    template_name = 'catalog/feature_form.html'

class FeatureEditView(g.UpdateView):
    model = Feature
    template_name = 'catalog/feature_form.html'

class FeatureDeleteView(g.DeleteView):
    model = Feature
    template_name = 'catalog/feature_confirm_delete.html'