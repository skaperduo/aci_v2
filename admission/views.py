from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Programs, SHSstrands, PreferredShift, YearLevel, GradeLevel, StudentClassification,\
    StudentPersonalInformation, SeniorHighSchool_StudentPersonalInformation, JuniorHighSchool_StudentPersonalInformation,\
    Elementary_StudentPersonalInformation, WhereDidYouHearUs, WhyDidYouChooseUs, SchoolYear

from .forms import StudentPersonalInformationForm, SHS_StudentPersonalInformationForm,\
    JHS_StudentPersonalInformationForm, ELEM_StudentPersonalInformationForm


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

        if form.is_valid():
            form.save()
            subject = "ACI Online Pre-registration Confirmation"
            message = "Thank you for Pre-registering to ACI \n " \
                      "Looking forward to seeing you in ACI Campus! \n God bless.."
            from_email = 'aciunofficial@gmail.com'
            email = form['email_address'].value()
            to_list = [email, settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

        return redirect('confirm')
        # return render(request, 'admission.html', {
        #     'programs': all_programs,
        #     'shifts': all_shifts,
        #     'year_level': all_year_level,
        #     'classification': all_classification,
        #     'where': all_where,
        #     'why': all_why
        # })

    else:
        return render(request, 'admission.html', {
            'programs': all_programs,
            'shifts': all_shifts,
            'year_level': all_year_level,
            'classification': all_classification,
            'where': all_where,
            'why': all_why,
            'school_year': school_year
        })


def confirmation(request):
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

        if form.is_valid():
            form.save()
            subject = "ACI Online Pre-registration Confirmation"
            message = "Thank you for Pre-registering to ACI \n " \
                      "Looking forward to seeing you in ACI Campus! \n God bless.."
            from_email = 'aciunofficial@gmail.com'
            email = form['shs_email_address'].value()
            to_list = [email, settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

        return redirect('confirm')
        # return render(request, 'admission.html', {
        #     'programs': all_programs,
        #     'shifts': all_shifts,
        #     'year_level': all_year_level,
        #     'classification': all_classification,
        #     'where': all_where,
        #     'why': all_why
        # })

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

        if form.is_valid():
            form.save()
            subject = "ACI Online Pre-registration Confirmation"
            message = "Thank you for Pre-registering to ACI \n " \
                      "Looking forward to seeing you in ACI Campus! \n God bless.."
            from_email = 'aciunofficial@gmail.com'
            email = form['jhs_email_address'].value()
            to_list = [email, settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

        return redirect('confirm')
        # return render(request, 'admission.html', {
        #     'programs': all_programs,
        #     'shifts': all_shifts,
        #     'year_level': all_year_level,
        #     'classification': all_classification,
        #     'where': all_where,
        #     'why': all_why
        # })

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

        if form.is_valid():
            form.save()
            subject = "ACI Online Pre-registration Confirmation"
            message = "Thank you for Pre-registering to ACI \n " \
                      "Looking forward to seeing you in ACI Campus! \n God bless.."
            from_email = 'aciunofficial@gmail.com'
            email = form['elementary_email_address'].value()
            to_list = [email, settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

        return redirect('confirm')
        # return render(request, 'admission.html', {
        #     'programs': all_programs,
        #     'shifts': all_shifts,
        #     'year_level': all_year_level,
        #     'classification': all_classification,
        #     'where': all_where,
        #     'why': all_why
        # })

    else:
        return render(request, 'elementary_admission.html', {
            'grade_level': all_grade_level,
            'classification': all_classification,
            'where': all_where,
            'why': all_why,
            'school_year': school_year
        })

