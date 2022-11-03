from django.contrib import admin

from students.models import Student, FlowTypes, ContingentFlow, FinanceForm, AbsentReason, Absents

admin.site.register(Student)
admin.site.register(FlowTypes)
admin.site.register(ContingentFlow)
admin.site.register(FinanceForm)
admin.site.register(AbsentReason)
admin.site.register(Absents)
