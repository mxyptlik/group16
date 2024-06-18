from django.contrib import admin
from.models import Employee,HourlyEmployee,Department,Contract_consultant,Dependent,Project,Works_on,Salaried_Employee,department_Employee
# Register your models here.

admin.site.register(Employee)
admin.site.register(HourlyEmployee)
admin.site.register(Department)
admin.site.register(Contract_consultant)
admin.site.register(Dependent)
admin.site.register(Project)
admin.site.register(Works_on)
admin.site.register(Salaried_Employee)
admin.site.register(department_Employee)

