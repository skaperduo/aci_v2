from django.urls import path
from . import views

urlpatterns = [
    path('', views.programs, name="programs"),
    path('program-beed', views.program_beed, name="program_beed"),
    path('program-bsed', views.program_bsed, name="program_bsed"),
    path('program-bsba', views.program_bsba, name="program_bsba"),
    path('program-bsais', views.program_bsais, name="program_bsais"),
    path('program-bsit', views.program_bsit, name="program_bsit"),
    path('program-maed', views.program_maed, name="program_maed"),
    path('program-mba', views.program_mba, name="program_mba"),
]
