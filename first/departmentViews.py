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
   

class addDepartment(View):
    model = Department,first_department
    form_class = first_departmentForm
    template = 'Dashboard/addDepartment.html'
    success_url = 'Dashboard/success.html'

    def get(self,request):
        departments = self.form_class()
        return render(request, 'Dashboard/addDepartment.html')
    
    def post(self,request):
        departments = self.form(request.POST, request.FILES)
        
        if departments.is_valid():
            departments.save()
            return redirect(request, 'Dashboard/success.html')
        
        return render(request, 'Dashboard/addDepartment.html' )
    


def removeDepartment(request , pk):
    department = Department.objects.get(pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('/home')
    return render(request, 'Dashboard/removeDepartment.html')

def manageDepartments(request, pk):
    department = Department.objects.get(pk=pk)
    if request.method == 'POST':
          department.delete()
          return redirect('/home')
    return render(request,'Dashboard/manageDepartments.html')


def departmentList(request):
    departments = Department.objects.all()
    context = {'departments' : departments}
    return render(request, 'Dashboard/departmentList.html',context)
 
