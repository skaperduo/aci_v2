# Generated by Django 3.0.5 on 2020-05-14 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0039_auto_20200514_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='GradStudentPersonalInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grad_last_name', models.CharField(max_length=255)),
                ('grad_first_name', models.CharField(max_length=255)),
                ('grad_middle_name', models.CharField(max_length=255)),
                ('grad_birthdate', models.CharField(max_length=255)),
                ('grad_birth_place', models.CharField(max_length=255)),
                ('grad_religion', models.CharField(blank=True, max_length=255)),
                ('grad_nationality', models.CharField(max_length=255)),
                ('grad_gender', models.CharField(max_length=255)),
                ('grad_civil_status', models.CharField(max_length=255)),
                ('grad_email_address', models.CharField(max_length=255)),
                ('grad_social_media_accounts', models.CharField(blank=True, max_length=255)),
                ('grad_mobile_number', models.CharField(max_length=255)),
                ('grad_landline_number', models.CharField(blank=True, max_length=255)),
                ('grad_home_address', models.CharField(max_length=255)),
                ('connectivity', models.CharField(default='limited connectivity', max_length=255)),
                ('grad_date_registered', models.DateField(auto_now_add=True)),
                ('export_to_CSV', models.BooleanField(default=False)),
                ('stud_reference_no', models.CharField(blank=True, max_length=255)),
                ('grad_stud_classification', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='admission.StudentClassification')),
                ('grad_stud_program', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='admission.Programs')),
                ('grad_stud_shift', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='admission.PreferredShift')),
                ('grad_stud_year_level', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='admission.YearLevel')),
                ('grad_where_hear_us', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='admission.WhereDidYouHearUs')),
                ('stud_school_year', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='admission.SchoolYear')),
                ('why_choose_us', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='admission.WhyDidYouChooseUs')),
            ],
        ),
    ]
