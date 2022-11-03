from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from faculties.models import Group


class FinanceForm(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Форма финансирования"


class Student(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    group_id = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    snils = models.CharField(max_length=20)
    inn = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    finance_form = models.ForeignKey(FinanceForm, null=True, on_delete=models.SET_NULL)
    last_update = models.DateTimeField(default=timezone.now)
    deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.surname} {self.name} {self.middle_name}'

    class Meta:
        verbose_name_plural = "Студенты"
        ordering = ['surname', 'name']


class FlowTypes(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "События"


class ContingentFlow(models.Model):
    type = models.ForeignKey(FlowTypes, on_delete=models.CASCADE)
    date = models.DateField()
    details = models.CharField(max_length=500)
    last_update = models.DateTimeField(default=timezone.now)
    deleted = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.details

    class Meta:
        verbose_name_plural = "Движение студентов"


class AbsentReason(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Причины пропусков занятий"


class Absents(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    number = models.IntegerField()
    reason = models.ForeignKey(AbsentReason, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Пропуски занятий"
