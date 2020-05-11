from django.urls import path
from . import views

urlpatterns = [
    path('', views.admission, name="admission"),
    path('confirmation', views.confirmation, name="confirm"),
    path('admission_requirements', views.admission_requirements, name="admission_requirements"),
    path('basic_ed_admission_requirements', views.basic_ed_admission_requirements, name="basic_ed_admission_requirements"),
    path('senior_high_school_admission', views.shs_admission, name="shs_admission"),
    path('junior_high_school_admission', views.jhs_admission, name="jhs_admission"),
    path('elementary_admission', views.elementary_admission, name="elementary_admission"),
    path('pre_reg_landing_page', views.pre_reg_landing_page, name="pre_reg_landing_page"),
    path('college_grad_confirmation', views.college_grad_confirmation, name="college_grad_confirm"),
]
