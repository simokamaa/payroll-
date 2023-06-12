from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
import csv
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .forms import ManagerForm, EmployeesForm,DailyWorkForm, CommisionSalaryForm, FixedSalaryForm, AllowancesForm, DeductionsForm, SalaryDetailsForm, JobTypeForm, CommissionTemplatesForm, ManageSalaryForm, SelectDepartmentForm, PayrollSummaryForm, AdvanceSalaryForm, OvertimeForm, EmployeeAwardForm, AddExpensesForm, DepartmentForm , first_departmentForm
from .models import Manager, Employees, Commision_saraly, Fixed_saraly, allowances, deductions, salary_details, job_type, commission_templates, ManageSalary, SelectDepartment, PayrollSummary, AdvanceSalary,  overtime, employeeAward, addExpenses, Department,DailyWork,first_department
from fpdf import FPDF
from .models import Transaction


departments = Employees.objects.all()
managers = Manager.objects.all()
commision_saralies =  Commision_saraly.objects.all()
fixed_salaries = Fixed_saraly.objects.all()
allowanceses = allowances.objects.all()
deduction = deductions.objects.all()
salary_detail = salary_details.objects.all()
job_types = job_type.objects.all()
commission_template = commission_templates.objects.all()
manageSalaries =  ManageSalary.objects.all()
SelectDepartments = SelectDepartment.objects.all()
PayrollSummaries =  PayrollSummary.objects.all()
advanceSalaries =  AdvanceSalary.objects.all()
departments = Department.objects.all()
dailyWorks = DailyWork.objects.all()
first_departments = first_department.objects.all()
employees = Employees.objects.all()
context = {
        'employees' : employees,
        'departments' : departments,
        'managers' : managers,
        'commision_saralies' : commision_saralies,
        'fixed_salaries' :  fixed_salaries,
        'allowanceses' :  allowanceses,
        ' deductions' :  deduction,
        'salary_details' : salary_detail,
        'job_types' : job_types,
        'commission_templates' : commission_template,
        'manageSalaries ' :  manageSalaries,
        'SelectDepartments' :  SelectDepartments,
        'PayrollSummaries' : PayrollSummaries,
        'advanceSalaries' : advanceSalaries,
        'dailyWorks ' :  dailyWorks,
        'first_departments' :  first_departments  
        }
       


def image_upload(request):
    data = {}
    if not request.POST:
        return render(request,'Dashboard/addEmployee.html')
    try:
        image_file = request.FILES["image_file"]
        if not image_file.name.endswith('.jpg','.jpeg','.png'):
            #message error (request, 'FILE is not an image type')
            return render(request, 'Dashboard/addEmployee.html', {
                'error_message' : "that file is not in csv format",
            })
            
    except Exception as e:
        return render(request, 'Dashboard/addEmployee.html', {
            'error_message' : 'Error reading that file'
        })
    
    return render(request,'Dashboard/employeeList.html')

def upload_front_id_image(request):
    data={}
    if not request.POST:
        return render(request, 'Dashboard/addEmployee.html')
    try:
        front_id_image = request.FILES["front_id_image"]
        if not front_id_image.name.endswith('.jpg','.jpeg','.png'):
            #error message
            return render(request,'Dashboard/addEmployee.html',{
                'error message' : 'Error uploading the file'
            })
            
    except Exception as e:
        return render(request, 'Dashboard/addEmployee.html',{
            'error message' : 'error handling that file'
        })
    
    return render(request, 'Dashboard/employeeList.html', context)

def upload_back_id_image(request):
    data={}
    if not request.POST:
        return render(request, 'Dashboard/addEmployee.html')
    try:
        back_id_image = request.FILES["front_id_image"]
        if not back_id_image.name.endswith('.jpg','.jpeg','.png'):
            #error message
            return render(request,'Dashboard/addEmployee.html',{
                'error message' : 'Error uploading the file'
            })
            
    except Exception as e:
        return render(request, 'Dashboard/addEmployee.html',{
            'error message' : 'error handling that file'
        })
    
    return render(request, 'Dashboard/employeeList.html', context)

def create_employees():
    pass


def upload(request):
    data = {}
    if not request.POST:
        return render(request,'Dashboard/dailyRecord.html', context)
    try:
        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            #error message
            return render(request, 'Dashboard/dailyRecord.html', {
                'error_message' : 'file is not a csv format'
            })
            
        f = open("res.csv", "w")
        file_data = csv_file.read().decode('utf-8')
        f.write(file_data)
        f.close()
        
        all_employees = []
        
        employees = Employees.objects.all()
        
        if len(employees) == 0:
            create_employees()
        
        reader = csv.DictReader(open("res.csv", "w"))
        
        for row in reader:
            all_employees,created = Employees.object.get_or_create(
                first_name = row['Employees']
            )
            all_employees.append(all_employees)
    except Exception as e:
        return render(request, 'Dashboard/dailyRecord.html',{
            'error_message' : 'error reading that file'
        })
    
    return render(request, 'Dashboard/dailyRecord.html',{
        'employees' : all_employees
    })