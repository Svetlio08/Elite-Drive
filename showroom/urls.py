from django.urls import path, include

from showroom import views as v

urlpatterns = [
    path('list/', v.CollectionListView.as_view(), name='collection-list'),
    path('create/', v.CollectionCreateView.as_view(), name='collection-create'),
    path('<int:pk>/', include([
        path('detail/', v.CollectionDetailView.as_view(), name='collection-detail'),
        path('edit/', v.CollectionEditView.as_view(), name='collection-edit'),
        path('delete/', v.CollectionDeleteView.as_view(), name='collection-delete'),
    ]))
]