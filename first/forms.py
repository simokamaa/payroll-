from django import forms
from .models import Manager, Employees, Commision_saraly, Fixed_saraly, allowances, deductions, salary_details, job_type, commission_templates, ManageSalary, SelectDepartment ,PayrollSummary, AdvanceSalary, overtime, employeeAward, addExpenses, Department, DailyWork,first_department,Employee

class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = '__all__'

class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'

class CommisionSalaryForm(forms.ModelForm):
    class Meta:
        model = Commision_saraly
        fields = '__all__'

class FixedSalaryForm(forms.ModelForm):
    class Meta:
        model = Fixed_saraly
        fields = '__all__'

class AllowancesForm(forms.ModelForm):
    class Meta:
        model = allowances
        fields = '__all__'

class DeductionsForm(forms.ModelForm):
    class Meta:
        model = deductions
        fields = '__all__'

class SalaryDetailsForm(forms.ModelForm):
    class Meta:
        model = salary_details
        fields = '__all__'

class JobTypeForm(forms.ModelForm):
    class Meta:
        model = job_type
        fields = '__all__'

class CommissionTemplatesForm(forms.ModelForm):
    class Meta:
        model = commission_templates
        fields = '__all__'

class ManageSalaryForm(forms.ModelForm):
    class Meta:
        model = ManageSalary
        fields = '__all__'

class SelectDepartmentForm(forms.ModelForm):
    class Meta:
        model = SelectDepartment
        fields = '__all__'

class PayrollSummaryForm(forms.ModelForm):
    class Meta:
        model = PayrollSummary
        fields = '__all__'

class AdvanceSalaryForm(forms.ModelForm):
    class Meta:
        model = AdvanceSalary
        fields = '__all__'

class OvertimeForm(forms.ModelForm):
    class Meta:
        model = overtime
        fields = '__all__'

class EmployeeAwardForm(forms.ModelForm):
    class Meta:
        model = employeeAward
        fields = '__all__'

class AddExpensesForm(forms.ModelForm):
    class Meta:
        model = addExpenses
        fields = '__all__'

class first_departmentForm(forms.ModelForm):
   field = forms.CharField(min_length = 32, widget=forms.TextInput(
       attrs = {
           'placeholder':'field',
           'class':'form-control',
       }
   ),
       error_messages = {
           'required' : "This field is required",
           'invalid' : "This field is invalid",
   })

   #Metadata
   class Meta:
       model = first_department
       fields = []


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
class DailyWorkForm(forms.ModelForm):
    class Meta:
        model = DailyWork
        fields = '__all__'
        

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'