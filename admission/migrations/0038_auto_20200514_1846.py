# Generated by Django 3.0.5 on 2020-05-14 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0037_yearlevel_semester'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yearlevel',
            name='semester',
        ),
        migrations.AddField(
            model_name='schoolyear',
            name='semester',
            field=models.CharField(default='1st-semester', max_length=50),
        ),
    ]
