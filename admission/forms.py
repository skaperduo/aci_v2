from django import forms
from .models import Programs, SHSstrands, PreferredShift, YearLevel, GradeLevel, StudentClassification,\
    StudentPersonalInformation, SeniorHighSchool_StudentPersonalInformation, JuniorHighSchool_StudentPersonalInformation,\
    Elementary_StudentPersonalInformation, WhereDidYouHearUs, WhyDidYouChooseUs, SchoolYear, GradStudentPersonalInformation


class StudentPersonalInformationForm(forms.ModelForm):
    class Meta:
        model = StudentPersonalInformation

        fields = ['last_name',
                  'first_name',
                  'middle_name',
                  'birthdate',
                  'birth_place',
                  'religion',
                  'nationality',
                  'gender',
                  'civil_status',
                  'email_address',
                  'social_media_accounts',
                  'mobile_number',
                  'landline_number',
                  'home_address',
                  'stud_classification',
                  'stud_program',
                  'stud_shift',
                  'stud_year_level',
                  'where_hear_us',
                  'why_choose_us',
                  'connectivity',
                  'gadget',
                  'stud_school_year',
                  'export_to_CSV',
                  'stud_reference_no',
                  ]


class GradStudentPersonalInformationForm(forms.ModelForm):
    class Meta:
        model = GradStudentPersonalInformation

        fields = ['grad_last_name',
                  'grad_first_name',
                  'grad_middle_name',
                  'grad_birthdate',
                  'grad_birth_place',
                  'grad_religion',
                  'grad_nationality',
                  'grad_gender',
                  'grad_civil_status',
                  'grad_email_address',
                  'grad_social_media_accounts',
                  'grad_mobile_number',
                  'grad_landline_number',
                  'grad_home_address',
                  'grad_stud_classification',
                  'grad_stud_program',
                  'grad_stud_shift',
                  'grad_stud_year_level',
                  'where_hear_us',
                  'why_choose_us',
                  'connectivity',
                  'gadget',
                  'grad_stud_school_year',
                  'export_to_CSV',
                  'grad_stud_reference_no',
                  ]


class SHS_StudentPersonalInformationForm(forms.ModelForm):
    class Meta:
        model = SeniorHighSchool_StudentPersonalInformation

        fields = ['shs_last_name',
                  'shs_first_name',
                  'shs_middle_name',
                  'shs_birthdate',
                  'shs_birth_place',
                  'shs_religion',
                  'shs_nationality',
                  'shs_gender',
                  'shs_civil_status',
                  'shs_email_address',
                  'shs_social_media_accounts',
                  'shs_mobile_number',
                  'shs_landline_number',
                  'shs_home_address',
                  'shs_stud_classification',
                  'shs_stud_grade_level',
                  'shs_stud_strand',
                  'where_hear_us',
                  'why_choose_us',
                  'connectivity',
                  'gadget',
                  'shs_school_year',
                  'shs_reference_no',
                  ]


class JHS_StudentPersonalInformationForm(forms.ModelForm):
    class Meta:
        model = JuniorHighSchool_StudentPersonalInformation

        fields = ['jhs_last_name',
                  'jhs_first_name',
                  'jhs_middle_name',
                  'jhs_birthdate',
                  'jhs_birth_place',
                  'jhs_religion',
                  'jhs_nationality',
                  'jhs_gender',
                  'jhs_civil_status',
                  'jhs_email_address',
                  'jhs_social_media_accounts',
                  'jhs_mobile_number',
                  'jhs_landline_number',
                  'jhs_home_address',
                  'jhs_stud_classification',
                  'jhs_stud_grade_level',
                  'where_hear_us',
                  'why_choose_us',
                  'connectivity',
                  'gadget',
                  'jhs_school_year',
                  'jhs_reference_no',
                  ]


class ELEM_StudentPersonalInformationForm(forms.ModelForm):
    class Meta:
        model = Elementary_StudentPersonalInformation

        fields = ['elementary_last_name',
                  'elementary_first_name',
                  'elementary_middle_name',
                  'elementary_birthdate',
                  'elementary_birth_place',
                  'elementary_religion',
                  'elementary_nationality',
                  'elementary_gender',
                  'elementary_civil_status',
                  'elementary_email_address',
                  'elementary_social_media_accounts',
                  'elementary_mobile_number',
                  'elementary_landline_number',
                  'elementary_home_address',
                  'elementary_stud_classification',
                  'elementary_stud_grade_level',
                  'where_hear_us',
                  'why_choose_us',
                  'connectivity',
                  'gadget',
                  'elem_school_year',
                  'elem_reference_no',
                  ]