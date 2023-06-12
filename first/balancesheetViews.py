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
from django.db import models


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



def balance_sheet(request):
    assets = Transaction.objects.filter(type='ASSETS')
    liabilities = Transaction.objects.filter(type='LIABILITIES')
    equity = Transaction.objects.filter(type='EQUITY')
    revenue = Transaction.objects.filter(type='REVENUE')
    expenses = Transaction.objects.filter(type='EXPENSE')

    total_assets = assets.aggregate(total=models.Sum('amount'))['total'] or 0
    total_liabilities = liabilities.aggregate(total=models.Sum('amount'))['total'] or 0
    total_equity = equity.aggregate(total=models.Sum('amount'))['total'] or 0
    total_revenue = revenue.aggregate(total=models.Sum('amount'))['total'] or 0
    total_expenses = expenses.aggregate(total=models.Sum('amount'))['total'] or 0

    net_income = total_revenue - total_expenses
    total_liabilities_equity = total_liabilities + total_equity

    context = {
        'assets': assets,
        'liabilities': liabilities,
        'equity': equity,
        'revenue': revenue,
        'expenses': expenses,
        'total_assets': total_assets,
        'total_liabilities': total_liabilities,
        'total_equity': total_equity,
        'total_revenue': total_revenue,
        'total_expenses': total_expenses,
        'net_income': net_income,
        'total_liabilities_equity': total_liabilities_equity,
    }

    return render(request, 'Dashboard/balanceSheet.html', context)
