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
    all_school_year = SchoolYear.objects.all

    if request.method == "POST":
        # form = StudentPersonalInformationForm(request.POST or None)

        school_year = int(request.POST.get('stud_school_year'))
        classification = int(request.POST.get('stud_classification'))
        program = int(request.POST.get('stud_program'))
        year_level = int(request.POST.get('stud_year_level'))
        shift = int(request.POST.get('stud_shift'))
        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        birthdate = request.POST.get('birthdate')
        birth_place = request.POST.get('birth_place')
        religion = request.POST.get('religion')
        nationality = request.POST.get('nationality')
        gender = request.POST.get('gender')
        civil_status = request.POST.get('civil_status')
        email_address = request.POST.get('email_address')
        social_media_accounts = request.POST.get('social_media_accounts')
        mobile_number = request.POST.get('mobile_number')
        landline_number = request.POST.get('landline_number')
        home_address = request.POST.get('home_address')
        where_hear_us = int(request.POST.get('where_hear_us'))
        why_choose_us = int(request.POST.get('why_choose_us'))
        connectivity = request.POST.get('connectivity')
        reference_no1 = random.randint(1, 99)
        reference_no2 = random.randint(1, 99)

        ref_no = f'ACI-{last_name[:2].upper()}{reference_no1}{first_name[:4].upper()}{reference_no2}'
        print(ref_no)
        # return redirect('confirm')
        return render(request, 'confirmation.html', {
            'school_year': school_year,
            'classification': classification,
            'program': program,
            'year_level': year_level,
            'shift': shift,
            'last_name': last_name,
            'first_name': first_name,
            'middle_name': middle_name,
            'birthdate': birthdate,
            'birth_place': birth_place,
            'religion': religion,
            'nationality': nationality,
            'gender': gender,
            'civil_status': civil_status,
            'email_address': email_address,
            'social_media_accounts': social_media_accounts,
            'mobile_number': mobile_number,
            'landline_number': landline_number,
            'home_address': home_address,
            'where_hear_us': where_hear_us,
            'why_choose_us': why_choose_us,
            'connectivity': connectivity,
            'reference_no': ref_no,

            'programs': all_programs,
            'shifts': all_shifts,
            'year_levels': all_year_level,
            'classifications': all_classification,
            'where': all_where,
            'why': all_why,
            'school_years': all_school_year,
        })

    else:
        return render(request, 'admission.html', {
            'programs': all_programs,
            'shifts': all_shifts,
            'year_level': all_year_level,
            'classification': all_classification,
            'where': all_where,
            'why': all_why,
            'school_year': all_school_year,
        })


def confirmation(request):

    # reference_no1 = random.randint(1, 99)
    # reference_no2 = random.randint(1, 99)
    # reference_no3 = random.randint(1, 99)
    # last = "Chanjueco"
    # first = "Hamilcar"
    # middle = "Bucong"
    # print(f'ACI-{last[:2].upper()}{reference_no1}{first[:4].upper()}{reference_no2}')

    all_programs = Programs.objects.all
    all_shifts = PreferredShift.objects.all
    all_year_level = YearLevel.objects.all
    all_classification = StudentClassification.objects.all
    all_why = WhyDidYouChooseUs.objects.all
    all_where = WhereDidYouHearUs.objects.all
    all_school_year = SchoolYear.objects.all

    if request.method == "POST":
        form = StudentPersonalInformationForm(request.POST or None)

        last_name = request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        ref_id_no = request.POST.get('stud_reference_no')

        if form.is_valid():
            form.save()
            subject = "ACI Online Pre-registration Confirmation"
            message = "Dear " + last_name + ", " + first_name + " " + middle_name + \
                      "\n\nWelcome to ACI\n" \
                      "\nWe are delighted to received your application.\n\n" \
                      "Your registration is confirmed and complete!\n" \
                      "Here is your reference no. (" + ref_id_no + "), for easy reference.\n\n" \
                                                                   "below are ACI's Official Contact Number:\n\n" \
                                                                   "Registrar 342-8004\n" \
                                                                   "Accounting Office 342-5843\n" \
                                                                   "QA 225-2330\n" \
                                                                   "Mobile: 09483626888\n"
            from_email = 'aciunofficial@gmail.com'
            email = form['email_address'].value()
            to_list = [email, settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

        # return redirect('confirm')
        return render(request, 'college_grad_confirmation.html', {
            'last_name': last_name,
            'first_name': first_name,
            'middle_name': middle_name,
        })
    else:
        return render(request, 'confirmation.html', {
            'programs': all_programs,
            'shifts': all_shifts,
            'year_levels': all_year_level,
            'classifications': all_classification,
            'where': all_where,
            'why': all_why,
            'school_years': all_school_year
        })


def shs_admission(request):

    all_shs_strands = SHSstrands.objects.all
    all_grade_level = GradeLevel.objects.all
    all_classification = StudentClassification.objects.all
    all_why = WhyDidYouChooseUs.objects.all
    all_where = WhereDidYouHearUs.objects.all
    all_school_year = SchoolYear.objects.all

    if request.method == "POST":
        # form = StudentPersonalInformationForm(request.POST or None)

        school_year = int(request.POST.get('shs_school_year'))
        classification = int(request.POST.get('shs_stud_classification'))
        grade_level = int(request.POST.get('shs_stud_grade_level'))
        strand = int(request.POST.get('shs_stud_strand'))
        last_name = request.POST.get('shs_last_name')
        first_name = request.POST.get('shs_first_name')
        middle_name = request.POST.get('shs_middle_name')
        birthdate = request.POST.get('shs_birthdate')
        birth_place = request.POST.get('shs_birth_place')
        religion = request.POST.get('shs_religion')
        nationality = request.POST.get('shs_nationality')
        gender = request.POST.get('shs_gender')
        civil_status = request.POST.get('shs_civil_status')
        email_address = request.POST.get('shs_email_address')
        social_media_accounts = request.POST.get('shs_social_media_accounts')
        mobile_number = request.POST.get('shs_mobile_number')
        landline_number = request.POST.get('shs_landline_number')
        home_address = request.POST.get('shs_home_address')
        where_hear_us = int(request.POST.get('where_hear_us'))
        why_choose_us = int(request.POST.get('why_choose_us'))
        connectivity = request.POST.get('connectivity')
        reference_no1 = random.randint(1, 99)
        reference_no2 = random.randint(1, 99)

        ref_no = f'ACI-{last_name[:2].upper()}{reference_no1}{first_name[:4].upper()}{reference_no2}'
        print(ref_no)
        # return redirect('confirm')
        return render(request, 'shs_confirmation.html', {
            'school_year': school_year,
            'classification': classification,
            'grade_level': grade_level,
            'strand': strand,
            'last_name': last_name,
            'first_name': first_name,
            'middle_name': middle_name,
            'birthdate': birthdate,
            'birth_place': birth_place,
            'religion': religion,
            'nationality': nationality,
            'gender': gender,
            'civil_status': civil_status,
            'email_address': email_address,
            'social_media_accounts': social_media_accounts,
            'mobile_number': mobile_number,
            'landline_number': landline_number,
            'home_address': home_address,
            'where_hear_us': where_hear_us,
            'why_choose_us': why_choose_us,
            'connectivity': connectivity,
            'reference_no': ref_no,

            'strands': all_shs_strands,
            'grade_levels': all_grade_level,
            'classifications': all_classification,
            'where': all_where,
            'why': all_why,
            'school_years': all_school_year,
        })

    else:
        return render(request, 'shs_admission.html', {
            'strands': all_shs_strands,
            'grade_level': all_grade_level,
            'classification': all_classification,
            'where': all_where,
            'why': all_why,
            'school_year': all_school_year,
        })


def shs_confirmation(request):

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
        ref_id_no = request.POST.get('shs_reference_no')

        if form.is_valid():
            form.save()
            subject = "ACI Online Pre-registration Confirmation"
            message = "Dear " + shs_last_name + ", " + shs_first_name + " " + shs_middle_name + \
                      "\n\nWelcome to ACI\n" \
                      "\nWe are delighted to received your application.\n\n" \
                      "Your registration is confirmed and complete!\n" \
                      "Here is your reference no. (" + ref_id_no + "), for easy reference.\n\n" \
                                                                   "below are ACI's Official Contact Number:\n\n" \
                                                                   "Registrar 342-8004\n" \
                                                                   "Accounting Office 342-5843\n" \
                                                                   "QA 225-2330\n" \
                                                                   "Mobile: 09483626888\n"
            from_email = 'aciunofficial@gmail.com'
            email = form['shs_email_address'].value()
            to_list = [email, settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

        # return redirect('confirm')
        return render(request, 'college_grad_confirmation.html', {
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
    all_school_year = SchoolYear.objects.all

    if request.method == "POST":
        # form = StudentPersonalInformationForm(request.POST or None)

        school_year = int(request.POST.get('jhs_school_year'))
        classification = int(request.POST.get('jhs_stud_classification'))
        grade_level = int(request.POST.get('jhs_stud_grade_level'))
        last_name = request.POST.get('jhs_last_name')
        first_name = request.POST.get('jhs_first_name')
        middle_name = request.POST.get('jhs_middle_name')
        birthdate = request.POST.get('jhs_birthdate')
        birth_place = request.POST.get('jhs_birth_place')
        religion = request.POST.get('jhs_religion')
        nationality = request.POST.get('jhs_nationality')
        gender = request.POST.get('jhs_gender')
        civil_status = request.POST.get('jhs_civil_status')
        email_address = request.POST.get('jhs_email_address')
        social_media_accounts = request.POST.get('jhs_social_media_accounts')
        mobile_number = request.POST.get('jhs_mobile_number')
        landline_number = request.POST.get('jhs_landline_number')
        home_address = request.POST.get('jhs_home_address')
        where_hear_us = int(request.POST.get('where_hear_us'))
        why_choose_us = int(request.POST.get('why_choose_us'))
        connectivity = request.POST.get('connectivity')
        reference_no1 = random.randint(1, 99)
        reference_no2 = random.randint(1, 99)

        ref_no = f'ACI-{last_name[:2].upper()}{reference_no1}{first_name[:4].upper()}{reference_no2}'
        print(ref_no)
        # return redirect('confirm')
        return render(request, 'jhs_confirmation.html', {
            'school_year': school_year,
            'classification': classification,
            'grade_level': grade_level,
            'last_name': last_name,
            'first_name': first_name,
            'middle_name': middle_name,
            'birthdate': birthdate,
            'birth_place': birth_place,
            'religion': religion,
            'nationality': nationality,
            'gender': gender,
            'civil_status': civil_status,
            'email_address': email_address,
            'social_media_accounts': social_media_accounts,
            'mobile_number': mobile_number,
            'landline_number': landline_number,
            'home_address': home_address,
            'where_hear_us': where_hear_us,
            'why_choose_us': why_choose_us,
            'connectivity': connectivity,
            'reference_no': ref_no,

            'grade_levels': all_grade_level,
            'classifications': all_classification,
            'where': all_where,
            'why': all_why,
            'school_years': all_school_year,
        })

    else:
        return render(request, 'jhs_admission.html', {
            'grade_level': all_grade_level,
            'classification': all_classification,
            'where': all_where,
            'why': all_why,
            'school_year': all_school_year,
        })


def jhs_confirmation(request):

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
        ref_id_no = request.POST.get('jhs_reference_no')

        if form.is_valid():
            form.save()
            subject = "ACI Online Pre-registration Confirmation"
            message = "Dear " + jhs_last_name + ", " + jhs_first_name + " " + jhs_middle_name + \
                      "\n\nWelcome to ACI\n" \
                      "\nWe are delighted to received your application.\n\n" \
                      "Your registration is confirmed and complete!\n" \
                      "Here is your reference no. (" + ref_id_no + "), for easy reference.\n\n" \
                                                                   "below are ACI's Official Contact Number:\n\n" \
                                                                   "Registrar 342-8004\n" \
                                                                   "Accounting Office 342-5843\n" \
                                                                   "QA 225-2330\n" \
                                                                   "Mobile: 09483626888\n"
            from_email = 'aciunofficial@gmail.com'
            email = form['jhs_email_address'].value()
            to_list = [email, settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

        # return redirect('confirm')
        return render(request, 'college_grad_confirmation.html', {
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
    all_school_year = SchoolYear.objects.all

    if request.method == "POST":
        # form = StudentPersonalInformationForm(request.POST or None)

        school_year = int(request.POST.get('elem_school_year'))
        classification = int(request.POST.get('elementary_stud_classification'))
        grade_level = int(request.POST.get('elementary_stud_grade_level'))
        last_name = request.POST.get('elementary_last_name')
        first_name = request.POST.get('elementary_first_name')
        middle_name = request.POST.get('elementary_middle_name')
        birthdate = request.POST.get('elementary_birthdate')
        birth_place = request.POST.get('elementary_birth_place')
        religion = request.POST.get('elementary_religion')
        nationality = request.POST.get('elementary_nationality')
        gender = request.POST.get('elementary_gender')
        civil_status = request.POST.get('elementary_civil_status')
        email_address = request.POST.get('elementary_email_address')
        social_media_accounts = request.POST.get('elementary_social_media_accounts')
        mobile_number = request.POST.get('elementary_mobile_number')
        landline_number = request.POST.get('elementary_landline_number')
        home_address = request.POST.get('elementary_home_address')
        where_hear_us = int(request.POST.get('where_hear_us'))
        why_choose_us = int(request.POST.get('why_choose_us'))
        connectivity = request.POST.get('connectivity')
        reference_no1 = random.randint(1, 99)
        reference_no2 = random.randint(1, 99)

        ref_no = f'ACI-{last_name[:2].upper()}{reference_no1}{first_name[:4].upper()}{reference_no2}'
        print(ref_no)
        # return redirect('confirm')
        return render(request, 'elem_confirmation.html', {
            'school_year': school_year,
            'classification': classification,
            'grade_level': grade_level,
            'last_name': last_name,
            'first_name': first_name,
            'middle_name': middle_name,
            'birthdate': birthdate,
            'birth_place': birth_place,
            'religion': religion,
            'nationality': nationality,
            'gender': gender,
            'civil_status': civil_status,
            'email_address': email_address,
            'social_media_accounts': social_media_accounts,
            'mobile_number': mobile_number,
            'landline_number': landline_number,
            'home_address': home_address,
            'where_hear_us': where_hear_us,
            'why_choose_us': why_choose_us,
            'connectivity': connectivity,
            'reference_no': ref_no,

            'grade_levels': all_grade_level,
            'classifications': all_classification,
            'where': all_where,
            'why': all_why,
            'school_years': all_school_year,
        })

    else:
        return render(request, 'elementary_admission.html', {
            'grade_level': all_grade_level,
            'classification': all_classification,
            'where': all_where,
            'why': all_why,
            'school_year': all_school_year,
        })


def elem_confirmation(request):

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
        ref_id_no = request.POST.get('elem_reference_no')

        if form.is_valid():
            form.save()
            subject = "ACI Online Pre-registration Confirmation"
            message = "Dear " + elementary_last_name + ", " + elementary_first_name + " " + elementary_middle_name + \
                      "\n\nWelcome to ACI\n" \
                      "\nWe are delighted to received your application.\n\n" \
                      "Your registration is confirmed and complete!\n\n" \
                      "Here is your reference no. (" + ref_id_no + "), for easy reference.\n\n" \
                                                                   "below are ACI's Official Contact Number:\n\n" \
                                                                   "Registrar 342-8004\n" \
                                                                   "Accounting Office 342-5843\n" \
                                                                   "QA 225-2330\n" \
                                                                   "Mobile: 09483626888\n"
            from_email = 'aciunofficial@gmail.com'
            email = form['elementary_email_address'].value()
            to_list = [email, settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

        # return redirect('confirm')
        return render(request, 'college_grad_confirmation.html', {
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


def college_grad_confirmation(request):
    return render(request, 'college_grad_confirmation.html', {})


def admission_requirements(request):
    return render(request, 'admission_requirements.html', {})


def basic_ed_admission_requirements(request):
    return render(request, 'basic_ed_admission_requirements.html', {})


def pre_reg_landing_page(request):
    return render(request, 'pre_reg_landing_page.html', {})

