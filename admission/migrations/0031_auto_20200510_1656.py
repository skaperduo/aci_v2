# Generated by Django 3.0.5 on 2020-05-10 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0030_elementary_studentpersonalinformation_reference_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='elementary_studentpersonalinformation',
            old_name='reference_no',
            new_name='elem_reference_no',
        ),
        migrations.AddField(
            model_name='juniorhighschool_studentpersonalinformation',
            name='jhs_reference_no',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='seniorhighschool_studentpersonalinformation',
            name='shs_reference_no',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='studentpersonalinformation',
            name='stud_reference_no',
            field=models.CharField(default=None, max_length=255),
        ),
    ]