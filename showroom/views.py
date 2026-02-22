from django.views import generic as g

from .models import Collection

class CollectionListView(g.ListView):
    model = Collection
    template_name = 'showroom/collection_list.html'

class CollectionDetailView(g.DetailView):
    model = Collection
    template_name = 'showroom/collection_detail.html'

class CollectionCreateView(g.CreateView):
    model = Collection
    template_name = 'showroom/collection_form.html'

class CollectionEditView(g.UpdateView):
    model = Collection
    template_name = 'showroom/collection_form.html'

class CollectionDeleteView(g.DeleteView):
    model = Collection
    template_name = 'showroom/collection_confirm_delete.html'