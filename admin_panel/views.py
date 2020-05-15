from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, Count, F
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

from admission.forms import StudentPersonalInformationForm, SHS_StudentPersonalInformationForm,\
    JHS_StudentPersonalInformationForm, ELEM_StudentPersonalInformationForm

from .forms import UserRegistrationForm
from admission.models import Programs, SHSstrands, PreferredShift, YearLevel, GradeLevel, StudentClassification, \
    StudentPersonalInformation, SeniorHighSchool_StudentPersonalInformation, \
    JuniorHighSchool_StudentPersonalInformation, \
    Elementary_StudentPersonalInformation, WhereDidYouHearUs, WhyDidYouChooseUs, SchoolYear, Appointment_Dates
from django.http import HttpResponse
import csv


# Create your views here.


def is_valid_queryparam(param):
    return param != '' and param is not None


@login_required
def admin_panel(request):
    count = request.GET.get('count')

    qs = StudentPersonalInformation.objects.all().order_by('date_registered')
    # qs_count = StudentPersonalInformation.objects.order_by('date_registered')[:int(count)]
    stud_programs = Programs.objects.all()

    # paginator = Paginator(qs, 4)
    # page = request.GET.get('page')
    # try:
    #     SPI = paginator.page(page)
    # except PageNotAnInteger:
    #     SPI = paginator.page(1)
    # except EmptyPage:
    #     SPI = paginator.page(paginator.num_pages)
    #
    # print(qs)
    # date = Appointment_Dates.objects.filter(pk=12).update(appointment_count=F('appointment_count') - 1)
    # Appointment_Dates.objects.filter(pk=12).update(appointment_count=)
    # print(date)

    key = request.GET.get('pk')
    last_name = request.GET.get('last_name')
    first_name = request.GET.get('first_name')
    middle_name = request.GET.get('middle_name')
    stud_program = request.GET.get('stud_program')
    stud_year_level = request.GET.get('stud_year_level')
    connectivity = request.GET.get('connectivity')
    date_registered = request.GET.get('date_registered')
    export = request.GET.get('export_to_CSV')

    if is_valid_queryparam(stud_program) and stud_program != 'Choose...':
        qs = qs.filter(stud_program__program_title=stud_program)

    if is_valid_queryparam(connectivity) and connectivity != 'Choose...':
        qs = qs.filter(connectivity__icontains=connectivity)

    if is_valid_queryparam(date_registered):
        qs = qs.filter(date_registered=date_registered)

    if is_valid_queryparam(count):
        qs = qs.order_by('date_registered')[:int(count)]

    context = {
        'queryset': qs,
        # 'spi': SPI,
        'stud_programs': stud_programs,
    }

    # if request.method == "GET":
    #     form = StudentPersonalInformationForm(request.GET or None)
    if export == 'on':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="College Pre-registration.csv"'
        writer = csv.writer(response)
        writer.writerow(['LAST NAME', 'FIRST NAME', 'MIDDLE NAME', 'PROGRAM', 'YEAR LEVEL', 'CONNECTIVITY',
                         'DATE REGISTERED', 'MOBILE #', 'REFERENCE #'])
        instance = qs
        for row in instance:
            writer.writerow([row.last_name, row.first_name, row.middle_name, row.stud_program, row.stud_year_level,
                             row.connectivity, row.date_registered, row.mobile_number, row.stud_reference_no])
        return response

    return render(request, 'admin_panel.html', context)


def under_graduate_admin_panel(request):
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


def shs_admin_panel(request):
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


def jhs_admin_panel(request):
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


def elem_admin_panel(request):
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


# def export(request):
#     order = request.GET.get('order')
#     print(order)
#     sort_direction = order[0]['dir']
#     sort_column = order[0]['column']
#     arr = ["first_name", "last_name", 'middle_name', 'stud_program', 'stud_year_level', 'connectivity']
#     data = StudentPersonalInformation.objects.order_by(arr[sort_column], sort_direction).values(
#         "first_name", "last_name", 'middle_name', 'stud_program', 'stud_year_level', 'connectivity'
#     )
#     paginator = Paginator(data, request.GET.get('length'))
#     page_number = request.GET.get('start')+1
#     page_obj = paginator.get_page(page_number)
#     # data_list = list(page_obj)
#     return JsonResponse(page_obj, safe=False)

