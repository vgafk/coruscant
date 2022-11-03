from django.db import models
from django.utils import timezone
from subjects.models import Discipline
from students.models import Student


class MarkType(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Типы оценок"


class Marks(models.Model):
    discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    type = models.ForeignKey(MarkType, on_delete=models.CASCADE)
    value = models.IntegerField()
    semester = models.IntegerField()
    last_update = models.DateTimeField(default=timezone.now)
    deleted = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Оценки студентов"
