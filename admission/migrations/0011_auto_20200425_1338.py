# Generated by Django 3.0.5 on 2020-04-25 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0010_auto_20200422_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentpersonalinformation',
            name='landline_number',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='studentpersonalinformation',
            name='religion',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='studentpersonalinformation',
            name='social_media_accounts',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
