# Generated by Django 4.1.3 on 2022-11-03 10:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Форма обучения',
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Факультеты',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('study_year', models.IntegerField()),
                ('last_update', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
                ('education_form', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='faculties.educationform')),
                ('faculty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculties.faculty')),
                ('study_plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='subjects.studyplan')),
            ],
            options={
                'verbose_name_plural': 'Группы',
            },
        ),
    ]
