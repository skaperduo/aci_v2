from django.urls import path
from . import views

urlpatterns = [
    path('', views.programs, name="programs"),
    path('program_beed', views.program_beed, name="program_beed"),
    path('program_bsed', views.program_bsed, name="program_bsed"),
    path('program_bsba', views.program_bsba, name="program_bsba"),
    path('program_bsais', views.program_bsais, name="program_bsais"),
    path('program_bsit', views.program_bsit, name="program_bsit"),
]
