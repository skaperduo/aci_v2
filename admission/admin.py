from django.contrib import admin
from .models import Programs, PreferredShift, YearLevel, StudentClassification, StudentPersonalInformation, WhereDidYouHearUs, WhyDidYouChooseUs


class SPIAdmin(admin.ModelAdmin):
    list_filter = ('stud_program', 'connectivity',)


admin.site.register(Programs)
admin.site.register(PreferredShift)
admin.site.register(YearLevel)
admin.site.register(StudentClassification)
admin.site.register(StudentPersonalInformation, SPIAdmin)
admin.site.register(WhereDidYouHearUs)
admin.site.register(WhyDidYouChooseUs)


# Register your models here.
