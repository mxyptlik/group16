# forms.py
from django import forms
from django.forms import ModelForm
from .models import department, Employee, Salaried_Employee, HourlyEmployee, Contract_consultant, Dependent, Project, Works_on, department_Employee

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = department
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class SalariedEmployeeForm(forms.ModelForm):
    class Meta:
        model = Salaried_Employee
        fields = '__all__'

class HourlyEmployeeForm(forms.ModelForm):
    class Meta:
        model = HourlyEmployee
        fields = '__all__'

class ContractConsultantForm(forms.ModelForm):
    class Meta:
        model = Contract_consultant
        fields = '__all__'

class DependentForm(forms.ModelForm):
    class Meta:
        model = Dependent
        fields = '__all__'

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class WorksOnForm(forms.ModelForm):
    class Meta:
        model = Works_on
        fields = '__all__'

class DepartmentEmployeeForm(forms.ModelForm):
    class Meta:
        model = department_Employee
        fields = '__all__'
