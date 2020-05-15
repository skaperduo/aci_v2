from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Programs, SHSstrands, PreferredShift, YearLevel, GradeLevel, StudentClassification,\
    StudentPersonalInformation, SeniorHighSchool_StudentPersonalInformation, JuniorHighSchool_StudentPersonalInformation,\
    Elementary_StudentPersonalInformation, WhereDidYouHearUs, WhyDidYouChooseUs, SchoolYear, Appointment_Dates,\
    Admission_Appointments, GradStudentPersonalInformation


class SPIAdmin(admin.ModelAdmin):
    ordering = ['date_registered']
    list_per_page = 10
    list_display = ('last_name', 'first_name', 'middle_name', 'stud_program', 'connectivity', 'date_registered',
                    'mobile_number', 'stud_reference_no')
    list_filter = ('stud_program', 'connectivity', 'date_registered')


class Grad_SPIAdmin(admin.ModelAdmin):
    ordering = ['grad_date_registered']
    list_per_page = 10
    list_display = ('grad_last_name', 'grad_first_name', 'grad_middle_name', 'grad_stud_program', 'connectivity',
                    'grad_date_registered', 'grad_mobile_number', 'grad_stud_reference_no')
    list_filter = ('grad_stud_program', 'connectivity', 'grad_date_registered')


class SHS_SPIAdmin(admin.ModelAdmin):
    ordering = ['shs_date_registered']
    list_per_page = 10
    list_display = ('shs_last_name', 'shs_first_name', 'shs_middle_name', 'shs_stud_grade_level', 'shs_stud_strand',
                    'connectivity', 'shs_date_registered', 'shs_mobile_number', 'shs_reference_no')
    list_filter = ('shs_stud_grade_level', 'shs_stud_strand', 'connectivity', 'shs_date_registered')


class JHS_SPIAdmin(admin.ModelAdmin):
    ordering = ['jhs_date_registered']
    list_per_page = 10
    list_display = ('jhs_last_name', 'jhs_first_name', 'jhs_middle_name', 'jhs_stud_grade_level',
                    'connectivity', 'jhs_date_registered', 'jhs_mobile_number', 'jhs_reference_no')
    list_filter = ('jhs_stud_grade_level', 'connectivity', 'jhs_date_registered')


class E_SPIAdmin(admin.ModelAdmin):
    ordering = ['elementary_date_registered']
    list_per_page = 10
    list_display = ('elementary_last_name', 'elementary_first_name', 'elementary_middle_name',
                    'elementary_stud_grade_level', 'connectivity', 'elementary_date_registered',
                    'elementary_mobile_number', 'elem_reference_no')
    list_filter = ('elementary_stud_grade_level', 'connectivity', 'elementary_date_registered')


class school_year(admin.ModelAdmin):
    list_display = ('school_year', 'semester', 'sy_status')


@admin.register(GradStudentPersonalInformation)
class Grad_SPIAdminPanel(ImportExportActionModelAdmin, Grad_SPIAdmin):
    pass


@admin.register(StudentPersonalInformation)
class SPIAdminPanel(ImportExportActionModelAdmin, SPIAdmin):
    pass


@admin.register(SeniorHighSchool_StudentPersonalInformation)
class SHS_SPIAdminPanel(ImportExportActionModelAdmin, SHS_SPIAdmin):
    pass


@admin.register(JuniorHighSchool_StudentPersonalInformation)
class JHS_SPIAdminPanel(ImportExportActionModelAdmin, JHS_SPIAdmin):
    pass


@admin.register(Elementary_StudentPersonalInformation)
class E_SPIAdminPanel(ImportExportActionModelAdmin, E_SPIAdmin):
    pass

# admin.site.register(StudentPersonalInformation, SPIAdmin)
# admin.site.register(SeniorHighSchool_StudentPersonalInformation, SHS_SPIAdmin)
# admin.site.register(JuniorHighSchool_StudentPersonalInformation, JHS_SPIAdmin)
# admin.site.register(Elementary_StudentPersonalInformation, E_SPIAdmin)


admin.site.register(Programs)
admin.site.register(PreferredShift)
admin.site.register(YearLevel)
admin.site.register(SHSstrands)
admin.site.register(GradeLevel)
admin.site.register(StudentClassification)
admin.site.register(WhereDidYouHearUs)
admin.site.register(WhyDidYouChooseUs)
# admin.site.register(SchoolYear, school_year)
admin.site.register(Appointment_Dates)
admin.site.register(Admission_Appointments)


@admin.register(SchoolYear)
class SchoolYear(school_year):
    pass


# Register your models here.
