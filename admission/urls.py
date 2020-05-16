from django.urls import path
from . import views

urlpatterns = [
    path('', views.admission, name="admission"),
    path('confirmation', views.confirmation, name="confirm"),
    path('admission-requirements', views.admission_requirements, name="admission_requirements"),
    path('basic-ed-admission-requirements', views.basic_ed_admission_requirements, name="basic_ed_admission_requirements"),
    path('grad-admission', views.grad_admission, name="grad_admission"),
    path('grad-confirmation', views.grad_confirmation, name="grad_confirm"),
    path('senior-high-school-admission', views.shs_admission, name="shs_admission"),
    path('junior-high-school-admission', views.jhs_admission, name="jhs_admission"),
    path('elementary-admission', views.elementary_admission, name="elementary_admission"),
    path('pre-reg-landing-page', views.pre_reg_landing_page, name="pre_reg_landing_page"),
    path('college-grad-confirmation', views.college_grad_confirmation, name="college_grad_confirm"),
    path('shs-confirmation', views.shs_confirmation, name="shs_confirm"),
    path('jhs-confirmation', views.jhs_confirmation, name="jhs_confirm"),
    path('elem-confirmation', views.elem_confirmation, name="elem_confirm"),
]
