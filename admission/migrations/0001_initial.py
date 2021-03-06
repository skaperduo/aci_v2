# Generated by Django 3.0.5 on 2020-04-21 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PreferredShirt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift_title', models.CharField(max_length=2)),
                ('shift_time', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Programs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StudentClassification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='YearLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_level', models.CharField(max_length=50)),
            ],
        ),
    ]
