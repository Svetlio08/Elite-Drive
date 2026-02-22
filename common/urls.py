from django.urls import path
from common import views as v

urlpatterns = [
    path("", v.HomeView.as_view(), name="home"),
]