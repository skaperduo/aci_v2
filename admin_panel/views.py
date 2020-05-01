from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from .forms import UserRegistrationForm
from admission.models import Programs, PreferredShift, YearLevel, StudentClassification, StudentPersonalInformation, WhereDidYouHearUs, WhyDidYouChooseUs

# Create your views here.


def is_valid_queryparam(param):
    return param != '' and param is not None


def admin_panel(request):
    qs = StudentPersonalInformation.objects.all()
    stud_programs = Programs.objects.all()

    key = request.GET.get('pk')
    last_name = request.GET.get('last_name')
    first_name = request.GET.get('first_name')
    middle_name_name = request.GET.get('middle_name')
    stud_program = request.GET.get('stud_program')
    stud_year_level = request.GET.get('stud_year_level')
    connectivity = request.GET.get('connectivity')
    date_registered = request.GET.get('date_registered')

    if is_valid_queryparam(stud_program) and stud_program != 'Choose...':
        qs = qs.filter(stud_program__program_title=stud_program)

    if is_valid_queryparam(connectivity) and connectivity != 'Choose...':
        qs = qs.filter(connectivity__icontains=connectivity)

    if is_valid_queryparam(date_registered):
        qs = qs.filter(date_registered=date_registered)

    context = {
        'queryset': qs,
        'stud_programs': stud_programs,
    }
    return render(request, 'admin_panel.html', context)


# def register_view(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('home')
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'register.html', {'form': form})

