from django.urls import path, include

from catalog import views as v

brands_urls = [
    path('', v.BrandListView.as_view(), name='brand-list'),
    path('Create/', v.BrandCreateView.as_view(), name='brand-create'),
    path('<int:pk>/', include([
        path('Edit/', v.BrandEditView.as_view(), name='brand-edit'),
        path('Delete/', v.BrandDeleteView.as_view(), name='brand-delete'),
    ])),
]

Features_urls = [
    path('', v.FeatureListView.as_view(), name='feature-list'),
    path('Create/', v.FeatureCreateView.as_view(), name='feature-create'),
    path('<int:pk>/', include([
        path('Edit/', v.FeatureEditView.as_view(), name='feature-edit'),
        path('Delete/', v.FeatureDeleteView.as_view(), name='feature-delete'),
    ]))
]

urlpatterns = [
    path('brands/', include(brands_urls)),
    path('Features/', include(Features_urls)),
]