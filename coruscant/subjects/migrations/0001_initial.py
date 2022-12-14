# Generated by Django 4.1.3 on 2022-11-03 10:48

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('code', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Направления подготовки',
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('last_update', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Дисциплины',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='EducationalProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('start_year', models.IntegerField()),
                ('end_year', models.IntegerField()),
                ('last_update', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.direction')),
            ],
            options={
                'verbose_name_plural': 'Образовательные программы',
            },
        ),
        migrations.CreateModel(
            name='StudyPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('start_year', models.IntegerField()),
                ('end_year', models.IntegerField()),
                ('last_update', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
                ('educational_program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.educationalprogram')),
            ],
            options={
                'verbose_name_plural': 'Учебные планы',
            },
        ),
        migrations.CreateModel(
            name='StudyPlanDisciplines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField()),
                ('last_update', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.discipline')),
                ('study_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.studyplan')),
            ],
            options={
                'verbose_name_plural': 'Связь УП и дисциплин',
            },
        ),
    ]
