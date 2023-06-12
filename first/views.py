from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
import csv
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .forms import ManagerForm, EmployeesForm,DailyWorkForm, CommisionSalaryForm, FixedSalaryForm, AllowancesForm, DeductionsForm, SalaryDetailsForm, JobTypeForm, CommissionTemplatesForm, ManageSalaryForm, SelectDepartmentForm, PayrollSummaryForm, AdvanceSalaryForm, OvertimeForm, EmployeeAwardForm, AddExpensesForm, DepartmentForm , first_departmentForm,EmployeeForm
from .models import Manager, Employees, Commision_saraly, Fixed_saraly, allowances, deductions, salary_details, job_type, commission_templates, ManageSalary, SelectDepartment, PayrollSummary, AdvanceSalary,  overtime, employeeAward, addExpenses, Department,DailyWork,first_department,Employee
from fpdf import FPDF
from .models import Transaction
from django.urls import path,include




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
       
   
   

# Create your views here.

def index(request):
    employees = Employees.objects.all()
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
    return render(request, 'Dashboard/index.html', context)


def salaryTemplates(request):
    return render(request, 'Dashboard/salaryTemplates.html' , context)

def commisionTemplates(request):
    return render(request, 'Dashboard/commisionTemplates.html',context)

def manageSalary(request):
    form = ManageSalaryForm()
    if request.method == 'POST':
        form=ManageSalaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
        else:
            form=ManageSalaryForm()
        
    return render(request,'Dashboard/manageSalary.html', {'form' : form})

def employeeSalaryList(request):
    employees = Employees.objects.all()
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
    return render(request, 'Dashboard/employeeSalaryList.html', context)

def makePayment(request):
    return render(request, 'Dashboard/makePayment.html', context)

def search_bar(request):
    return render(request, 'Dashboard/index.html') 

def payrollSummary(request):
    return render (request, 'Dashboard/payrollSummary.html', context)

def advanceSalary(request):
    return render(request, 'Dashboard/advanceSalary.html', context)

def providentFund(request):
    return render(request, 'Dashboard/providentFund.html', context)


def commisionList(request):
    employees = Employees.object.all()
    context = {
        'employees' : employees
    }
    return render(request,'Dashboard/commisionList.html', context)

def makePaymentList(request):
    employees = Employees.object.all()
    context = {
        'employees' : employees
    }
    return render(request, 'Dashboard/makePayementList.html', context)

def manageSalaryList(request):
    employees = Employees.objects.all()
    persentage_commision = Commision_saraly.objects.all()
    context = {
        'employees' : employees, 
        'persentage_commisions' : persentage_commision
        }
    return render(request, 'Dashboard/manageSalaryList.html', context)

def set_tax(request):
    return render(request,'Dashboard/commisionTemplates.html', context)


#end of daily record


def salary_report(request, period):
    employees = Employees.objects.all()
    context = {
        'employees': employees,
        'period': period,
    }
    return render(request, 'Dashboard/salary_report.html', context)


def dailyReports(request):
    return render(request, 'Dashboard/dailyReports.html', context)

def monthlyReports(request):
    return render(request, 'Dashboard/monthlyReports.html', context)

def yearlyReports(request):
    return render(request , 'Dashboard/yearlyReports.html', context)

def needHelp(request):
    return render(request,'Dashboard/needHelp.html')

def settings(request):
    return render(request, 'Dashboard/settings.html', context)


def profile(request):
    managers =  Manager.objects.all()
    context = {
        'managers' : managers
    }
    return render(request, 'Dashboard/profile.html', context)

def sign_out(request):
   return render(request, 'Dashboard/logout.html')

