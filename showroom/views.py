from django.urls import reverse_lazy
from django.views import generic as g

from .models import Collection
import showroom.forms as f


class CollectionListView(g.ListView):
    model = Collection
    template_name = "showroom/collection_list.html"
    context_object_name = "collections"
    ordering = ["-is_featured", "title"]


class CollectionDetailView(g.DetailView):
    model = Collection
    template_name = "showroom/collection_detail.html"
    context_object_name = "collection"


class CollectionCreateView(g.CreateView):
    model = Collection
    form_class = f.CollectionForm
    template_name = "showroom/collection_form.html"
    success_url = reverse_lazy("collection-list")


class CollectionEditView(g.UpdateView):
    model = Collection
    form_class = f.CollectionForm
    template_name = "showroom/collection_form.html"
    success_url = reverse_lazy("collection-list")


class CollectionDeleteView(g.DeleteView):
    model = Collection
    template_name = "showroom/collection_confirm_delete.html"
    success_url = reverse_lazy("collection-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = f.CollectionDeleteForm(instance=self.object)
        return context