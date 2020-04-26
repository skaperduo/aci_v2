from django.urls import path
from . import views

urlpatterns = [
    path('', views.admission, name="admission"),
    path('confirmation', views.confirmation, name="confirm"),
    path('admission_requirements', views.admission_requirements, name="admission_requirements")
]
