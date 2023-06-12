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
       
def generatePayslip(request):
    employees = Employees.objects.all()
    return render(request,'Dashboard/generatePayslip.html', {'employees' : employees})
      

def generate_payslip(request,pk):
    # Get the required data for the payslip (replace with your own logic to fetch the data)
    company_name = "STYLUSH HAIR AND BEAUTY COLLEGE"
    employee = get_object_or_404(Employees, pk=pk)
    generation_date = "May 25, 2023"
    tax_amount = "Kshs 100.00"
    allowance = "Kshs  500.00"
    commission = "Kshs 200.00"
    company_logo = "path/to/company_logo.png"

    # Create a PDF object
    pdf = FPDF()

    # Create the first page
    pdf.add_page()

    # Create the payslip HTML template
    payslip_template = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Payslip</title>
            <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
        </head>
        <body>
            <div class="container mt-5">
                <div class="row">
                    <div class="col-md-6 offset-md-3 text-center mb-4">
                        <img src="{company_logo}" class="img-fluid" alt="Company Logo">
                        <h4 class="mt-3">{company_name}</h4>
                    </div>
                </div>
                <div class="row">
                    
                        <h5 class="text-center">Full Names: {employee.first_name} {employee.middle_name} {employee.last_name}</h5>
                        <p class="text-center">Employement ID: {employee.Employement_id}</p>
                        <p class="text-center">Email: {employee.Email }</p>
                        <p class="text-center">Date of Generation: {generation_date}</p>
                        <p class="text-center">Tax Amount: {tax_amount}</p>
                        <p class="text-center">Allowance: {allowance}</p>
                        <p class="text-center">Monthly Commission: {commission}</p>
                    </div>
                </div>
            </div>
        </body>
        </html>
    """

    # Generate the PDF response
    pdf.add_page()
    pdf.write_html(payslip_template)

    # Create the response with the PDF content
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=payslip.pdf'
    pdf.output(response)
    return response
   
