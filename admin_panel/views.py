from django.shortcuts import render, redirect
from admission.models import Programs, PreferredShift, YearLevel, StudentClassification, StudentPersonalInformation, WhereDidYouHearUs, WhyDidYouChooseUs

# Create your views here.


def admin_panel(request):
    return render(request, 'admin_panel.html', {})

