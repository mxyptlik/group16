from django.db import models

import random

# Create your models here.

def gen_id(iden):
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)

    final = iden + str(a) + str(b) + str(c)

    return final

class Department(models.Model):
    department_id = models.CharField(max_length=15, primary_key = True, null = False, blank= False)
    department_name = models.CharField(max_length = 50, null = False, blank = False)
    department_location = models.TextField(blank=False)

    def __str__(self):
        return f'{self.department_id}'





class Employee(models.Model):
    EMPLOYEE_TYPE = [
        ("Hourly", "Hourly Employee"),
        ("Salaried", "Salaried Employee"),
        ("Contract", "Contract Employee"),
    ]
    GENDER = [
        ('M','male'),
        ('F','female'),
    ]

    Employee_id = models.CharField(primary_key = True, default=gen_id('E'), max_length=10, unique=True)
    department_id = models.ForeignKey(Department, null = False,  blank = False,on_delete =models.CASCADE)
    FirstName = models.CharField(max_length=255, blank=False)
    LastName = models.CharField(max_length=255, blank=False)
    MiddleName = models.CharField(max_length=255, blank=False)
    Address = models.TextField(blank=False)
    Employee_type = models.name = models.CharField(max_length=10,null=True, choices =EMPLOYEE_TYPE )
    gender = models.CharField(max_length=1,null =True, choices = GENDER)
    salary = models.DecimalField(max_digits =16,decimal_places = 2)
    birthdate = models.DateField(blank = False)

    def __str__(self):
        return f'{self.Employee_id}'
    
    
    def save(self, *args, **kwargs):
        if self.Employee_type == 'Hourly':
            self.Employee_id = gen_id('EH')
        elif self.Employee_type == 'Salaried':
            self.Employee_id = gen_id('ES')
        elif self.Employee_type == 'Contract':
            self.Employee_id = gen_id('EC')

        super().save(*args, **kwargs)
                 


    
    class Meta:
     unique_together = ['Employee_id','department_id']





class Salaried_Employee(models.Model):
    Employee_id = models.ForeignKey(Employee,null = False, blank = False,on_delete =models.CASCADE)
    AnnualSalary = models.DecimalField(max_digits =10,decimal_places = 2 )
    StockOption =    models.DecimalField(max_digits =10,decimal_places = 2 )

    def __str__(self):
        return f'{self.Employee_id.FirstName} {self.Employee_id.LastName} ({self.Employee_id})'

class HourlyEmployee(models.Model):
    Employee_id = models.ForeignKey(Employee,null = False, blank = False, on_delete =models.CASCADE)
    HourlyRate =    models.DecimalField(max_digits =10,decimal_places = 2 )

    def __str__(self):
        return f'{self.Employee_id.FirstName} {self.Employee_id.LastName} ({self.Employee_id})'

class Contract_consultant(models.Model):
    Employee_id = models.ForeignKey(Employee,null = False, blank = False, on_delete =models.CASCADE)
    BillingRate =    models.DecimalField(max_digits =4,decimal_places = 2 )
    Contract_number =models.CharField(max_length =7, null = False, blank = False)

    def __str__(self):
        return f'{self.Employee_id.FirstName} {self.Employee_id.LastName} ({self.Employee_id})'


class Dependent(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    Dependent_id = models.CharField(primary_key = True, default=gen_id('DE'), max_length=10, unique=True)
    Employee_id = models.ForeignKey(Employee,null = False, blank = False,on_delete =models.CASCADE)
    Dependent_Name = models.CharField(max_length=255, blank=False)
    Dependent_gender = models.CharField(max_length=1, null=True, choices=GENDER_CHOICES)
    Dependent_birthdate = models.DateField(blank=False)
    Dependent_Relationship = models.CharField(max_length=255, blank=False)

    
    def __str__(self):
        return f'{self.Dependent_id}'


class Project(models.Model):
    project_id =  models.CharField(primary_key = True, default=gen_id('P'), max_length=10, unique=True)
    department_id = models.ForeignKey(Department, null = False,  blank = False,on_delete =models.CASCADE)
    project_name = models.CharField(max_length=100, blank = False)
    ProjectLocation = models.CharField(max_length=200, blank = False)

    def __str__(self):
        return f'{self.project_id}'

class Works_on(models.Model):
    work_id = models.CharField(primary_key = True, default=gen_id('W'), max_length=10, unique=True)
    Employee_id = models.ForeignKey(Employee,null = False, blank = False,on_delete =models.CASCADE)
    project_id = models.ForeignKey(Project,null = False, blank = False,on_delete =models.CASCADE)
    department_id = models.ForeignKey(Department, null = False,  blank = False,on_delete =models.CASCADE)

class department_Employee(models.Model):
    EMPLOYEE_TYPE = [
        ("Hourly", "Hourly Employee"),
        ("Salaried", "Salaried Employee"),
        ("Contract", "Contract Employee"),
    ]
        
        
    EmployeeDepartment_id = models.CharField(max_length=10,primary_key = True)
    Employee_id = models.ForeignKey(Employee, null = False, blank = False, on_delete =models.CASCADE)
    department_id = models.ForeignKey(Department, null = False,  blank = False,on_delete =models.CASCADE)
    FirstName = models.CharField(max_length=255, blank=False)
    department_name = models.CharField(max_length = 50, null = False, blank = False)
    Employee_type = models.name = models.CharField(max_length=10,null=True, choices =EMPLOYEE_TYPE )

    class Meta:
     unique_together = ['Employee_id','FirstName']

