from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('homepage', views.homepage, name="homepage")
]
