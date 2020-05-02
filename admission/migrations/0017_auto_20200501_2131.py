# Generated by Django 3.0.5 on 2020-05-01 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0016_auto_20200501_2024'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_year', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='elementary_studentpersonalinformation',
            name='school_year',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='admission.SchoolYear'),
        ),
        migrations.AlterField(
            model_name='juniorhighschool_studentpersonalinformation',
            name='school_year',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='admission.SchoolYear'),
        ),
        migrations.AlterField(
            model_name='seniorhighschool_studentpersonalinformation',
            name='school_year',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='admission.SchoolYear'),
        ),
        migrations.AlterField(
            model_name='studentpersonalinformation',
            name='school_year',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='admission.SchoolYear'),
        ),
    ]