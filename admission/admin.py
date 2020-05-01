from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Programs, PreferredShift, YearLevel, StudentClassification, StudentPersonalInformation, WhereDidYouHearUs, WhyDidYouChooseUs


class SPIAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'stud_program', 'connectivity', 'date_registered')
    list_filter = ('stud_program', 'connectivity', 'date_registered')


@admin.register(StudentPersonalInformation)
class SPIAdminPanel(ImportExportActionModelAdmin, SPIAdmin):
    pass


admin.site.register(Programs)
admin.site.register(PreferredShift)
admin.site.register(YearLevel)
admin.site.register(StudentClassification)
admin.site.register(WhereDidYouHearUs)
admin.site.register(WhyDidYouChooseUs)


# Register your models here.
