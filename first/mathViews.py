from .forms import *
from .models import *
from .models import Transaction
import math
import statistics
from abc import ABC
from django.shortcuts import render,redirect




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
    

def calculate_daily_salary(request):
    persentage_commision = Commision_saraly.objects.all()
    daily_total_salary = persentage_commision/100 *DailyWork.total_amount
    weekly_salary = daily_total_salary * 7
   
def calculate_salary(request):
    if request.method == 'POST':
        form = SalaryDetailsForm(request.POST)
        if form.is_valid():
            salary = form.save(commit=False)
            net_salary = salary.gross_salary + salary.house_allowance + salary.medical_allowance - salary.provident_fund - salary.tax_deduction
            form.instance.net_salary = net_salary
            form.save()
            return render(request, 'Dashboard/salaryTemplates', {'net_salary': net_salary})
    else:
        form = SalaryDetailsForm()
    return render(request, 'Dashboard/salaryTemplates', {'form': form})

 #start of daily record
def employee_commision(request,pk):
    pass

def monthly_employee_commision(request,pk):
    pass


def commision_today(request):
    pass

def total_commision(request):
    pass

def calculate_income(request):
    pass

def monthly_income(request):
    pass

def calculate_total_income(request):
    pass

def total_employees(request):
    pass

def total_expenses(request):
    pass


def total_monthly_salary(request):
    pass