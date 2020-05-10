from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import permission_required
from .models import Programs, SHSstrands, PreferredShift, YearLevel, GradeLevel, StudentClassification,\
    StudentPersonalInformation, SeniorHighSchool_StudentPersonalInformation, JuniorHighSchool_StudentPersonalInformation,\
    Elementary_StudentPersonalInformation, WhereDidYouHearUs, WhyDidYouChooseUs, SchoolYear

from .forms import StudentPersonalInformationForm, SHS_StudentPersonalInformationForm,\
    JHS_StudentPersonalInformationForm, ELEM_StudentPersonalInformationForm

import random


# Create your views here.


# def admission(request):
#     all_programs = Programs.objects.all
#     all_shifts = PreferredShift.objects.all
#     all_year_level = YearLevel.objects.all
#     all_classification = StudentClassification.objects.all
#
#     return render(request, 'admission.html', {
#         'programs': all_programs,
#         'shifts': all_shifts,
#         'year_level': all_year_level,
#         'classification': all_classification
#     })


def admission(request):

    all_programs = Programs.objects.all
    all_shifts = PreferredShift.objects.all
    all_year_level = YearLevel.objects.all
    all_classification = StudentClassification.objects.all
    all_why = WhyDidYouChooseUs.objects.all
    all_where = WhereDidYouHearUs.objects.all
    school_year = SchoolYear.objects.all

    if request.method == "POST":
        form = StudentPersonalInformationForm(request.POST or None)

        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        # reference_no1 = random.randint(1, 99)
        # reference_no2 = random.randint(1, 99)
        #
        # ref_no = f'ACI-{last_name[:2].upper()}{reference_no1}{first_name[:4].upper()}{reference_no2}'
        # print(ref_no)

        if form.is_valid():
            form.save()
            subject = "ACI Online Pre-registration Confirmation"
            message = "Dear " + last_name + ", " + first_name + " " + middle_name + \
                      "\nWelcome to ACI \n " \
                      "We are delighted to received your application. \n \n" \
                      "Your registration is confirmed and complete!"
            from_email = 'aciunofficial@gmail.com'
            email = form['email_address'].value()
            to_list = [email, settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

        # return redirect('confirm')
        return render(request, 'confirmation.html', {
            'last_name': last_name,
            'first_name': first_name,
            'middle_name': middle_name,
        })

    else:
        return render(request, 'admission.html', {
            'programs': all_programs,
            'shifts': all_shifts,
            'year_level': all_year_level,
            'classification': all_classification,
            'where': all_where,
            'why': all_why,
            'school_year': school_year,
        })


def confirmation(request):

    # reference_no1 = random.randint(1, 99)
    # reference_no2 = random.randint(1, 99)
    # reference_no3 = random.randint(1, 99)
    # last = "Chanjueco"
    # first = "Hamilcar"
    # middle = "Bucong"
    # print(f'ACI-{last[:2].upper()}{reference_no1}{first[:4].upper()}{reference_no2}')

    return render(request, 'confirmation.html', {})


def admission_requirements(request):
    return render(request, 'admission_requirements.html', {})


def basic_ed_admission_requirements(request):
    return render(request, 'basic_ed_admission_requirements.html', {})


def shs_admission(request):

    all_shs_strands = SHSstrands.objects.all
    all_grade_level = GradeLevel.objects.all
    all_classification = StudentClassification.objects.all
    all_why = WhyDidYouChooseUs.objects.all
    all_where = WhereDidYouHearUs.objects.all
    school_year = SchoolYear.objects.all

    if request.method == "POST":
        form = SHS_StudentPersonalInformationForm(request.POST or None)

        shs_last_name = request.POST.get('shs_last_name')
        shs_first_name = request.POST.get('shs_first_name')
        shs_middle_name = request.POST.get('shs_middle_name')

        if form.is_valid():
            form.save()
            subject = "ACI Online Pre-registration Confirmation"
            message = "Dear " + shs_last_name + ", " + shs_first_name + " " + shs_middle_name + \
                      "\nWelcome to ACI \n " \
                      "We are delighted to received your application. \n \n" \
                      "Your registration is confirmed and complete!"
            from_email = 'aciunofficial@gmail.com'
            email = form['shs_email_address'].value()
            to_list = [email, settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

        # return redirect('confirm')
        return render(request, 'confirmation.html', {
            'last_name': shs_last_name,
            'first_name': shs_first_name,
            'middle_name': shs_middle_name,
        })

    else:
        return render(request, 'shs_admission.html', {
            'strands': all_shs_strands,
            'grade_level': all_grade_level,
            'classification': all_classification,
            'where': all_where,
            'why': all_why,
            'school_year': school_year
        })


def jhs_admission(request):
    all_grade_level = GradeLevel.objects.all
    all_classification = StudentClassification.objects.all
    all_why = WhyDidYouChooseUs.objects.all
    all_where = WhereDidYouHearUs.objects.all
    school_year = SchoolYear.objects.all

    if request.method == "POST":
        form = JHS_StudentPersonalInformationForm(request.POST or None)

        jhs_last_name = request.POST.get('jhs_last_name')
        jhs_first_name = request.POST.get('jhs_first_name')
        jhs_middle_name = request.POST.get('jhs_middle_name')

        if form.is_valid():
            form.save()
            subject = "ACI Online Pre-registration Confirmation"
            message = "Dear " + jhs_last_name + ", " + jhs_first_name + " " + jhs_middle_name + \
                      "\nWelcome to ACI \n " \
                      "We are delighted to received your application. \n \n" \
                      "Your registration is confirmed and complete!"
            from_email = 'aciunofficial@gmail.com'
            email = form['jhs_email_address'].value()
            to_list = [email, settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

        # return redirect('confirm')
        return render(request, 'confirmation.html', {
            'last_name': jhs_last_name,
            'first_name': jhs_first_name,
            'middle_name': jhs_middle_name,
        })

    else:
        return render(request, 'jhs_admission.html', {
            'grade_level': all_grade_level,
            'classification': all_classification,
            'where': all_where,
            'why': all_why,
            'school_year': school_year
        })


def elementary_admission(request):
    all_grade_level = GradeLevel.objects.all
    all_classification = StudentClassification.objects.all
    all_why = WhyDidYouChooseUs.objects.all
    all_where = WhereDidYouHearUs.objects.all
    school_year = SchoolYear.objects.all

    if request.method == "POST":
        form = ELEM_StudentPersonalInformationForm(request.POST or None)

        elementary_last_name = request.POST.get('elementary_last_name')
        elementary_first_name = request.POST.get('elementary_first_name')
        elementary_middle_name = request.POST.get('elementary_middle_name')

        if form.is_valid():
            form.save()
            subject = "ACI Online Pre-registration Confirmation"
            message = "Dear " + elementary_last_name + ", " + elementary_first_name + " " + elementary_middle_name + \
                      "\nWelcome to ACI \n " \
                      "We are delighted to received your application. \n \n" \
                      "Your registration is confirmed and complete!"
            from_email = 'aciunofficial@gmail.com'
            email = form['elementary_email_address'].value()
            to_list = [email, settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

        # return redirect('confirm')
        return render(request, 'confirmation.html', {
            'last_name': elementary_last_name,
            'first_name': elementary_first_name,
            'middle_name': elementary_middle_name,
        })

    else:
        return render(request, 'elementary_admission.html', {
            'grade_level': all_grade_level,
            'classification': all_classification,
            'where': all_where,
            'why': all_why,
            'school_year': school_year
        })


def pre_reg_landing_page(request):
    return render(request, 'pre_reg_landing_page.html', {})

