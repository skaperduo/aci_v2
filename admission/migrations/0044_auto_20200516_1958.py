# Generated by Django 3.0.5 on 2020-05-16 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0043_auto_20200515_0805'),
    ]

    operations = [
        migrations.AddField(
            model_name='elementary_studentpersonalinformation',
            name='gadget',
            field=models.CharField(default='None of the Above', max_length=255),
        ),
        migrations.AddField(
            model_name='gradstudentpersonalinformation',
            name='gadget',
            field=models.CharField(default='None of the Above', max_length=255),
        ),
        migrations.AddField(
            model_name='juniorhighschool_studentpersonalinformation',
            name='gadget',
            field=models.CharField(default='None of the Above', max_length=255),
        ),
        migrations.AddField(
            model_name='seniorhighschool_studentpersonalinformation',
            name='gadget',
            field=models.CharField(default='None of the Above', max_length=255),
        ),
        migrations.AddField(
            model_name='studentpersonalinformation',
            name='gadget',
            field=models.CharField(default='None of the Above', max_length=255),
        ),
    ]