from django.shortcuts import render, redirect, HttpResponse

from django.contrib import messages

from .models import (
    Employee,HourlyEmployee,Department,Contract_consultant,Dependent, Project,Works_on,Salaried_Employee,department_Employee
)


# Create your views here.
def home(request, *args, **kwargs):
    return render(request, 'home.html', {})

def employee(request, *args, **kwargs):

    if request.method == 'POST':
        data = request.POST
        
        print(data['department_id'])

        try:
            get_department = Department.objects.get(department_id=data['department_id'])
            
        except:
           messages.info(request, 'Invalid Department!')
           return redirect('employee')

        new_employee = Employee.objects.create(department_id=get_department, FirstName=data['FirstName'],
                                               LastName=data['LastName'], MiddleName=data['MiddleName'],
                                               Address=data['Address'], Employee_type=data['Employee_type'], 
                                               gender=data['gender'], salary=data['salary'], birthdate=data['birthdate'])
        
        request.session['employee'] = new_employee.Employee_id

        new_employee.save()
        
        return redirect('forms')

    return render(request, 'employee.html', {})

def dependent(request, *args, **kwargs):
    error = ''
    if request.method == 'POST':
        data = request.POST

        try:
            get_employee = Employee.objects.get(Employee_id=data['Employee_id'])
        except:   
            messages.info(request, "EmployeeID doesn't exist ! ")
            return redirect('dependent')                   
  

        print(data['birthdate'])
        new_dependent = Dependent.objects.create(Employee_id=get_employee, Dependent_Name=data['Dependent_Name'],
                                                Dependent_gender=data['Dependent_gender'],
                                                Dependent_Relationship=data['Dependent_Relationship'], Dependent_birthdate=data['birthdate'])
        
        new_dependent.save()


        return HttpResponse('Dependent created successfully')

    return render(request, 'dependent.html', {})

def department(request, *args, **kwargs):
    error =''
    if request.method =='POST':
        data = request.POST

        new_department = Department.objects.create( department_id= data['department_id'],department_name= data['department_name'],
                                                   department_location = data['department_location'])
        
        new_department.save()
        return HttpResponse('Department created successfully')
        

    return render(request, 'department.html', {})
    
def project(request, *args, **kwargs):
    error = ''
    
    if request.method =='POST':
        data = request.POST

        try:
            get_department = Department.objects.get(department_id=data['department_id'])
        except:
           messages.info(request, 'Invalid Department!')
           return redirect('project')
        
        new_project = Project.objects.create(department_id = get_department,project_name = data['project_name'], ProjectLocation = data['ProjectLocation'])
        new_project.save()

        return HttpResponse('Project created Succesfully')


    
    return render(request, 'project.html', {})

def works_on(request, *args, **kwargs):
    error = ''
    if request.method == 'POST':
        data = request.POST

        try:
            get_department = Department.objects.get(department_id=data['department_id'])
        except:
           messages.info(request, 'Invalid Department!')
           return redirect('works_on')
        
        try:
            get_employee = Employee.objects.get(Employee_id=data['Employee_id'])
        except:   
            messages.info(request, "EmployeeID doesn't exist ! ")
            return redirect('works_on')  
        
        try:
            get_project = Project.objects.get(project_id =data['project_id'] )
        except:
            messages.info(request, "ProjectID doesn't exist ! ")
            return redirect('works_on')     

        return HttpResponse('Joined Successfully')

    return render(request, 'works_on.html', {})




def forms(request,*args,**kwargs):
    employee = Employee.objects.get(Employee_id=request.session['employee'])    

    if request.method == 'POST':
        data = request.POST

        if employee.Employee_type == 'Salaried':
                new_salaried_employee = Salaried_Employee.objects.create(
                    Employee_id=employee,
                    AnnualSalary=data['AnnualSalary'],
                    StockOption=data['StockOption']
                )
                new_salaried_employee.save()
                return redirect('project')
        elif employee.Employee_type == 'Hourly':
                new_hourly_employee = HourlyEmployee.objects.create(
                    Employee_id=employee,
                    HourlyRate=data['HourlyRate']
                )
                new_hourly_employee.save()

                return redirect('project')
        elif employee.Employee_type == 'Contract':
                new_contract_employee = Contract_consultant.objects.create(
                    Employee_id=employee,
                    BillingRate=data['BillingRate'],
                    Contract_number=data['Contract_number']
                )
                new_contract_employee.save()

                return redirect('project')  



    return render(request,'forms.html',{'employee': employee})

