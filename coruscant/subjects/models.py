from django.utils import timezone
from django.db import models


class Direction(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    code = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return f'{self.code} {self.name}'

    class Meta:
        verbose_name_plural = "Направления подготовки"


class EducationalProgram(models.Model):
    name = models.CharField(max_length=50)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    last_update = models.DateTimeField(default=timezone.now)
    deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Образовательные программы"


class StudyPlan(models.Model):
    name = models.CharField(max_length=255)
    educational_program = models.ForeignKey(EducationalProgram, on_delete=models.CASCADE)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    last_update = models.DateTimeField(default=timezone.now)
    deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Учебные планы"


class Discipline(models.Model):
    name = models.CharField(max_length=255)
    last_update = models.DateTimeField(default=timezone.now)
    deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Дисциплины"
        ordering = ['name']


class StudyPlanDisciplines(models.Model):
    study_plan = models.ForeignKey(StudyPlan, on_delete=models.CASCADE)
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    semester = models.IntegerField()
    last_update = models.DateTimeField(default=timezone.now)
    deleted = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Связь УП и дисциплин"
