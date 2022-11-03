from django.db import models
from django.utils import timezone

from subjects.models import StudyPlan


class EducationForm(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Форма обучения"


class Faculty(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Факультеты"


class Group(models.Model):
    name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    faculty_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    study_year = models.IntegerField()
    education_form = models.ForeignKey(EducationForm, null=True, on_delete=models.SET_NULL)
    study_plan = models.ForeignKey(StudyPlan, null=True, on_delete=models.SET_NULL)
    last_update = models.DateTimeField(default=timezone.now)
    deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Группы"