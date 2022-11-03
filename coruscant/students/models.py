from django.db import models
from django.contrib.auth.models import User
from faculties.models import Group


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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Студенты"


# class Absents(Base):
#     __tablename__ = "absents"
#     id = Column(Integer, autoincrement=True, primary_key=True, index=True)
#     student_id = Column(Integer, index=True)
#     date = Column(Date, nullable=False)
#     number = Column(Integer, nullable=False)