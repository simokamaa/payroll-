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
       

def addExpenses(request):
    if request.method == 'POST':
        form = AddExpensesForm
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'Dashboard/addExpenses.html', context)

def expense_list(request):
    expenses =addExpenses.objects.all()
    return render(request, 'Dashboard/expensesList.html', {'expenses': expenses}, context)

def expense_create(request):
    form = AddExpensesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Dashboard/expensesList.html')
    return render(request,  'Dashboard/addExpenses.html', {'form': form}, context)

def expense_update(request, pk):
    expense = addExpenses.objects.get(pk=pk)
    form = AddExpensesForm(request.POST or None, instance=expense)
    if form.is_valid():
        form.save()
        return redirect('Dashboard/expensesList.html')
    return render(request,  'Dashboard/addExpenses.html', {'form': form}, context)

def expense_delete(request, pk):
    expense = addExpenses.objects.get(pk=pk)
    if request.method == 'POST':
        expense.delete()
        return redirect('Dashboard/expensesList.html')
    return render(request, 'expenses/expense_confirm_delete.html', {'expense': expense}, context)


def deleteAllExpenses(request):
    expensesList.objects.all().delete()

def expensesList(request):
    expenses = expenses.objects.all()
    context =  {'expenses' : expenses}
    return render(request,'Dashboard/expensesList.html', context)
