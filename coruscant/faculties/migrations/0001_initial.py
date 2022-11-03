# Generated by Django 4.1.3 on 2022-11-02 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('study_year', models.IntegerField()),
                ('faculty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='faculties.faculty')),
            ],
        ),
    ]