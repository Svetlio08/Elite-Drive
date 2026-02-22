from django.urls import path, include

from cars import views as v

urlpatterns = [
    path('list/', v.CarListView.as_view(), name='car-list'),
    path('create/', v.CarCreateView.as_view(), name='car-create'),
    path('<int:pk>/', include([
        path('', v.CarDetailView.as_view(), name='car-detail'),
        path('edit/', v.CarEditView.as_view(), name='car-edit'),
        path('delete/', v.CarDeleteView.as_view(), name='car-delete'),

    ])),
]