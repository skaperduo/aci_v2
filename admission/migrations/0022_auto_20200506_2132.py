# Generated by Django 3.0.5 on 2020-05-06 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0021_admission_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission_appointment',
            name='appointment_count',
            field=models.CharField(default='50', max_length=10),
        ),
        migrations.AlterField(
            model_name='admission_appointment',
            name='appointment_status',
            field=models.CharField(default='inactive', max_length=8),
        ),
    ]