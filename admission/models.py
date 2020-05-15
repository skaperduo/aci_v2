from django.db import models
from django.utils import timezone
from datetime import datetime, date

# Create your models here.


class Programs(models.Model):
    program_title = models.CharField(max_length=255)

    def __str__(self):
        return self.program_title


class SHSstrands(models.Model):
    strand_title = models.CharField(max_length=255)

    def __str__(self):
        return self.strand_title


class PreferredShift(models.Model):
    shift_title = models.CharField(max_length=50)
    shift_time = models.CharField(max_length=50)

    def __str__(self):
        return str(self.pk) + ' ' + self.shift_title + ' - ' + self.shift_time


class YearLevel(models.Model):
    year_level = models.CharField(max_length=50)

    def __str__(self):
        return self.year_level


class GradeLevel(models.Model):
    grade_level = models.CharField(max_length=50)

    def __str__(self):
        return self.grade_level


class StudentClassification(models.Model):
    classification = models.CharField(max_length=50)

    def __str__(self):
        return str(self.pk) + ' ' + self.classification


class WhereDidYouHearUs(models.Model):
    where = models.CharField(max_length=255)

    def __str__(self):
        return self.where


class WhyDidYouChooseUs(models.Model):
    why = models.CharField(max_length=255)

    def __str__(self):
        return self.why


class SchoolYear(models.Model):
    school_year = models.CharField(max_length=255)
    semester = models.CharField(max_length=50, default="1st-semester")
    sy_status = models.CharField(max_length=255, default="active")

    def __str__(self):
        return self.school_year + ' ' + self.semester


class StudentPersonalInformation(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    birthdate = models.CharField(max_length=255)
    birth_place = models.CharField(max_length=255)
    religion = models.CharField(max_length=255, blank=True)
    nationality = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    civil_status = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    social_media_accounts = models.CharField(max_length=255, blank=True)
    mobile_number = models.CharField(max_length=255)
    landline_number = models.CharField(max_length=255,blank=True)
    home_address = models.CharField(max_length=255)
    stud_classification = models.ForeignKey(StudentClassification, default=1, on_delete=models.SET_DEFAULT)
    stud_program = models.ForeignKey(Programs, default=1, on_delete=models.SET_DEFAULT)
    stud_shift = models.ForeignKey(PreferredShift, default=1, on_delete=models.SET_DEFAULT)
    stud_year_level = models.ForeignKey(YearLevel, default=1, on_delete=models.SET_DEFAULT)
    where_hear_us = models.ForeignKey(WhereDidYouHearUs, default=1, on_delete=models.SET_DEFAULT)
    why_choose_us = models.ForeignKey(WhyDidYouChooseUs, default=1, on_delete=models.SET_DEFAULT)
    connectivity = models.CharField(max_length=255, default="limited connectivity")
    stud_school_year = models.ForeignKey(SchoolYear, default=1, on_delete=models.SET_DEFAULT)
    date_registered = models.DateTimeField(auto_now_add=True, auto_now=False)
    export_to_CSV = models.BooleanField(default=False)
    stud_reference_no = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.pk) + ' ' + self.last_name + ', ' + self.first_name + ' ' + self.middle_name + ' ' + self.stud_reference_no
       # return str(self.pk) + ' ' + self.last_name + ', ' + self.first_name + ' ' + self.middle_name + ' ' + self.stud_reference_no


class GradStudentPersonalInformation(models.Model):
    grad_last_name = models.CharField(max_length=255)
    grad_first_name = models.CharField(max_length=255)
    grad_middle_name = models.CharField(max_length=255)
    grad_birthdate = models.CharField(max_length=255)
    grad_birth_place = models.CharField(max_length=255)
    grad_religion = models.CharField(max_length=255, blank=True)
    grad_nationality = models.CharField(max_length=255)
    grad_gender = models.CharField(max_length=255)
    grad_civil_status = models.CharField(max_length=255)
    grad_email_address = models.CharField(max_length=255)
    grad_social_media_accounts = models.CharField(max_length=255, blank=True)
    grad_mobile_number = models.CharField(max_length=255)
    grad_landline_number = models.CharField(max_length=255,blank=True)
    grad_home_address = models.CharField(max_length=255)
    grad_stud_classification = models.ForeignKey(StudentClassification, default=1, on_delete=models.SET_DEFAULT)
    grad_stud_program = models.ForeignKey(Programs, default=1, on_delete=models.SET_DEFAULT)
    grad_stud_shift = models.ForeignKey(PreferredShift, default=1, on_delete=models.SET_DEFAULT)
    grad_stud_year_level = models.ForeignKey(YearLevel, default=1, on_delete=models.SET_DEFAULT)
    where_hear_us = models.ForeignKey(WhereDidYouHearUs, default=1, on_delete=models.SET_DEFAULT)
    why_choose_us = models.ForeignKey(WhyDidYouChooseUs, default=1, on_delete=models.SET_DEFAULT)
    connectivity = models.CharField(max_length=255, default="limited connectivity")
    grad_stud_school_year = models.ForeignKey(SchoolYear, default=1, on_delete=models.SET_DEFAULT)
    grad_date_registered = models.DateTimeField(auto_now_add=True, auto_now=False)
    export_to_CSV = models.BooleanField(default=False)
    grad_stud_reference_no = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.pk) + ' ' + self.grad_last_name + ', ' + self.grad_first_name + ' ' + self.grad_middle_name + ' ' + self.grad_stud_reference_no


class SeniorHighSchool_StudentPersonalInformation(models.Model):
    shs_last_name = models.CharField(max_length=255)
    shs_first_name = models.CharField(max_length=255)
    shs_middle_name = models.CharField(max_length=255)
    shs_birthdate = models.CharField(max_length=255)
    shs_birth_place = models.CharField(max_length=255)
    shs_religion = models.CharField(max_length=255, blank=True)
    shs_nationality = models.CharField(max_length=255)
    shs_gender = models.CharField(max_length=255)
    shs_civil_status = models.CharField(max_length=255)
    shs_email_address = models.CharField(max_length=255)
    shs_social_media_accounts = models.CharField(max_length=255, blank=True)
    shs_mobile_number = models.CharField(max_length=255)
    shs_landline_number = models.CharField(max_length=255,blank=True)
    shs_home_address = models.CharField(max_length=255)
    shs_stud_classification = models.ForeignKey(StudentClassification, default=1, on_delete=models.SET_DEFAULT)
    shs_stud_grade_level = models.ForeignKey(GradeLevel, default=1, on_delete=models.SET_DEFAULT)
    shs_stud_strand = models.ForeignKey(SHSstrands, default=1, on_delete=models.SET_DEFAULT)
    where_hear_us = models.ForeignKey(WhereDidYouHearUs, default=1, on_delete=models.SET_DEFAULT)
    why_choose_us = models.ForeignKey(WhyDidYouChooseUs, default=1, on_delete=models.SET_DEFAULT)
    connectivity = models.CharField(max_length=255, default="limited connectivity")
    shs_school_year = models.ForeignKey(SchoolYear, default=1, on_delete=models.SET_DEFAULT)
    shs_date_registered = models.DateTimeField(auto_now_add=True, auto_now=False)
    export_to_CSV = models.BooleanField(default=False)
    shs_reference_no = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.pk) + ' ' + self.shs_last_name + ', ' + self.shs_first_name + ' ' + self.shs_middle_name
        # return str(self.pk) + ' ' + self.shs_last_name + ', ' + self.shs_first_name + ' ' + self.shs_middle_name + ' ' + self.shs_reference_no


class JuniorHighSchool_StudentPersonalInformation(models.Model):
    jhs_last_name = models.CharField(max_length=255)
    jhs_first_name = models.CharField(max_length=255)
    jhs_middle_name = models.CharField(max_length=255)
    jhs_birthdate = models.CharField(max_length=255)
    jhs_birth_place = models.CharField(max_length=255)
    jhs_religion = models.CharField(max_length=255, blank=True)
    jhs_nationality = models.CharField(max_length=255)
    jhs_gender = models.CharField(max_length=255)
    jhs_civil_status = models.CharField(max_length=255)
    jhs_email_address = models.CharField(max_length=255)
    jhs_social_media_accounts = models.CharField(max_length=255, blank=True)
    jhs_mobile_number = models.CharField(max_length=255)
    jhs_landline_number = models.CharField(max_length=255, blank=True)
    jhs_home_address = models.CharField(max_length=255)
    jhs_stud_classification = models.ForeignKey(StudentClassification, default=1, on_delete=models.SET_DEFAULT)
    jhs_stud_grade_level = models.ForeignKey(GradeLevel, default=1, on_delete=models.SET_DEFAULT)
    where_hear_us = models.ForeignKey(WhereDidYouHearUs, default=1, on_delete=models.SET_DEFAULT)
    why_choose_us = models.ForeignKey(WhyDidYouChooseUs, default=1, on_delete=models.SET_DEFAULT)
    connectivity = models.CharField(max_length=255, default="limited connectivity")
    jhs_school_year = models.ForeignKey(SchoolYear, default=1, on_delete=models.SET_DEFAULT)
    jhs_date_registered = models.DateTimeField(auto_now_add=True, auto_now=False)
    export_to_CSV = models.BooleanField(default=False)
    jhs_reference_no = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.pk) + ' ' + self.jhs_last_name + ', ' + self.jhs_first_name + ' ' + self.jhs_middle_name
        # return str(self.pk) + ' ' + self.jhs_last_name + ', ' + self.jhs_first_name + ' ' + self.jhs_middle_name + ' ' + self.jhs_reference_no


class Elementary_StudentPersonalInformation(models.Model):
    elementary_last_name = models.CharField(max_length=255)
    elementary_first_name = models.CharField(max_length=255)
    elementary_middle_name = models.CharField(max_length=255)
    elementary_birthdate = models.CharField(max_length=255)
    elementary_birth_place = models.CharField(max_length=255)
    elementary_religion = models.CharField(max_length=255, blank=True)
    elementary_nationality = models.CharField(max_length=255)
    elementary_gender = models.CharField(max_length=255)
    elementary_civil_status = models.CharField(max_length=255)
    elementary_email_address = models.CharField(max_length=255)
    elementary_social_media_accounts = models.CharField(max_length=255, blank=True)
    elementary_mobile_number = models.CharField(max_length=255)
    elementary_landline_number = models.CharField(max_length=255,blank=True)
    elementary_home_address = models.CharField(max_length=255)
    elementary_stud_classification = models.ForeignKey(StudentClassification, default=1, on_delete=models.SET_DEFAULT)
    elementary_stud_grade_level = models.ForeignKey(GradeLevel, default=1, on_delete=models.SET_DEFAULT)
    where_hear_us = models.ForeignKey(WhereDidYouHearUs, default=1, on_delete=models.SET_DEFAULT)
    why_choose_us = models.ForeignKey(WhyDidYouChooseUs, default=1, on_delete=models.SET_DEFAULT)
    connectivity = models.CharField(max_length=255, default="limited connectivity")
    elem_school_year = models.ForeignKey(SchoolYear, default=1, on_delete=models.SET_DEFAULT)
    elementary_date_registered = models.DateTimeField(auto_now_add=True, auto_now=False)
    export_to_CSV = models.BooleanField(default=False)
    elem_reference_no = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.pk) + ' ' + self.elementary_last_name + ', ' + self.elementary_first_name + ' ' + self.elementary_middle_name
        # return str(self.pk) + ' ' + self.elementary_last_name + ', ' + self.elementary_first_name + ' ' + self.elementary_middle_name + ' ' + self.elem_reference_no


class Appointment_Dates(models.Model):
    appointment_date = models.DateField(blank=True)
    appointment_status = models.CharField(max_length=8, default="inactive")
    appointment_count = models.IntegerField(default=50)

    def __str__(self):
        return str(self.pk) + ' ' + str(self.appointment_date) + ' ' + self.appointment_status + ' ' + str(self.appointment_count)


class Admission_Appointments(models.Model):
    student_id = models.ForeignKey(StudentPersonalInformation, default=1, on_delete=models.SET_DEFAULT)
    appointment_date_id = models.ForeignKey(Appointment_Dates, default=1, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return str(self.student_id) + ' ' + str(self.appointment_date_id)
