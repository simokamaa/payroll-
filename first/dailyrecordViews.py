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
       
   



def dailyRecord(request):
    if request.method == 'POST':
        form = DailyWorkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Dashboard/DailyRecordList.html')
    else:
        form = DailyWorkForm()
    return render(request, 'Dashboard/DailyRecord.html', {'form': form})

    

def dailywork_update(request, pk):
    dailywork = get_object_or_404(DailyWork, pk=pk)
    if request.method == 'POST':
        form = DailyWorkForm(request.POST, instance=dailywork)
        if form.is_valid():
            form.save()
            return redirect('Dashboard/DailyRecordList.html')
    else:
        form = DailyWorkForm(instance=dailywork)
    return render(request, 'dailywork/dailywork_form.html', {'form': form}, context)

def dailyRecordList(request):
    dailyworks = DailyWork.objects.all()
    return render(request, 'Dashboard/DailyRecordList.html', {'dailyworks': dailyworks})


def dailywork_delete(request, pk):
    dailywork = get_object_or_404(DailyWork, pk=pk)
    if request.method == 'POST':
        dailywork.delete()
        return redirect('Dashboard/DailyRecordList.html')
    return render(request, 'Dashboard/delete.html', {'dailywork': dailywork}, context)


def dailywork_detail(request, pk):
    dailywork = get_object_or_404(DailyWork, pk=pk)
    return render(request, 'Dashboard/dailywork_detail.html', {'dailywork': dailywork}, context)
