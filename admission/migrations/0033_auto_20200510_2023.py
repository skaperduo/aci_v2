# Generated by Django 3.0.5 on 2020-05-10 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0032_auto_20200510_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elementary_studentpersonalinformation',
            name='elem_reference_no',
        ),
        migrations.RemoveField(
            model_name='juniorhighschool_studentpersonalinformation',
            name='jhs_reference_no',
        ),
        migrations.RemoveField(
            model_name='seniorhighschool_studentpersonalinformation',
            name='shs_reference_no',
        ),
        migrations.RemoveField(
            model_name='studentpersonalinformation',
            name='stud_reference_no',
        ),
    ]