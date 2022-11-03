from django.utils import timezone
from django.db import models
from faculties.models import EducationForm


class Direction(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    code = models.CharField(max_length=20, null=False, blank=False)

    class Meta:
        verbose_name_plural = "Направления подготовки"


class EducationalProgram(models.Model):
    name = models.CharField(max_length=50)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    last_update = models.DateTimeField(default=timezone.now())
    deleted = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Образовательные программы"


class StudyPlan(models.Model):
    title = models.CharField(max_length=255)
    education_form = models.ForeignKey(EducationForm, on_delete=models.CASCADE)
    educational_program = models.ForeignKey(EducationalProgram, on_delete=models.CASCADE)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    last_update = models.DateTimeField(default=timezone.now())
    deleted = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Учебные планы"


class Discipline(models.Model):
    title = models.CharField(max_length=255)
    last_update = models.DateTimeField(default=timezone.now())
    deleted = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Дисциплины"


class StudyPlanDisciplines(models.Model):
    study_plan = models.ForeignKey(StudyPlan, on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    semester = models.IntegerField()
    last_update = models.DateTimeField(default=timezone.now())
    deleted = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Связь УП и дисциплин"
