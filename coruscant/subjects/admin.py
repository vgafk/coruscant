from django.contrib import admin
from .models import EducationalProgram, Direction, Discipline, StudyPlan, StudyPlanDisciplines

admin.site.register(EducationalProgram)
admin.site.register(Direction)
admin.site.register(Discipline)
admin.site.register(StudyPlan)
admin.site.register(StudyPlanDisciplines)
