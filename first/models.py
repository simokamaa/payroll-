from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

Employees = get_user_model()
Department = get_user_model()
job_type = get_user_model()

class Manager(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=128)
    password = models.IntegerField()
    confirm_password = models.IntegerField()

class Employees(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    Employement_id = models.IntegerField()
    Email = models.EmailField()
    phone_number = models.IntegerField()
    kra_pin = models.IntegerField()
    image = models.ImageField(upload_to='upload', default = 'a.png')
    front_id_image = models.ImageField(upload_to='upload',  default = 'a.png')
    back_id_image = models.ImageField(upload_to='upload',  default = 'a.png')
    salary=models.IntegerField()
    department = models.ForeignKey("Department", on_delete=models.CASCADE)
   
    def __str__(self):
        return self.first_name
    
class Commision_saraly(models.Model):
    single_work = models.FloatField()
    daily_work = models.FloatField()
    monthly_work = models.FloatField()

class Fixed_saraly(models.Model):
    single_work=models.FloatField()
    daily_work=models.FloatField()
    monthly_work=models.FloatField()
    
class allowances(models.Model):
    house_allowance = models.FloatField()
    medical_allowance = models.FloatField()

class deductions(models.Model):
    provident_fund = models.FloatField()
    tax_deduction = models.FloatField()

class salary_details(models.Model):
    gross_salary = models.FloatField()
    house_allowances = models.FloatField()
    medical_allowance = models.FloatField()
    provident_fund = models.FloatField()    
    tax_deductions = models.FloatField()
    

class job_type(models.Model):
    department = models.ForeignKey("Department", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    
    
class ManageSalary(models.Model):
    employee= models.ForeignKey("Employees", on_delete=models.CASCADE)
    job_type = models.ForeignKey("job_type", on_delete=models.CASCADE)
    amount = models.FloatField()

class SelectDepartment(models.Model):
    department = models.ForeignKey("Department", on_delete=models.CASCADE)
    select_month = models.DateField()
    
class PayrollSummary(models.Model):
    employeeId= models.ForeignKey("Employees", on_delete=models.CASCADE)

class AdvanceSalary(models.Model):
    employee_name = models.ForeignKey("Employees", on_delete=models.CASCADE)
    amount = models.FloatField()
    month=[]
    month = models.CharField(max_length=200)
    reason = models.CharField(max_length=2000)

class overtime(models.Model):
    employee_id =  models.ForeignKey("Employees", on_delete=models.CASCADE)
    date = models.DateField()
    Hour = models.DurationField()
    Text = models.TextField()
    
class employeeAward(models.Model):
    employee_name =  models.ForeignKey("Employees", on_delete=models.CASCADE)
    gift_item = models.CharField(max_length=200)
    month = models.DateField()
    month= models.DateField()
    award_date = models.DateField()
    
class addExpenses(models.Model):
    expense_name = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    amount = models.FloatField()
    text = models.CharField(max_length=2000000)
    
class Department(models.Model):
    name = models.CharField(max_length=255)
    id = models.IntegerField(primary_key=True)
    
    def __str__(self):
        return self.name
    
class first_department(models.Model):
    name = models.CharField(max_length=255)
    id = models.IntegerField(primary_key=True)
    
    def __str__(self):
        return self.name
    


    
class DailyWork(models.Model):
    employee_ID =  models.ForeignKey("Employees", on_delete=models.CASCADE)
    total_amount = models.FloatField()
<<<<<<< Updated upstream
    job_type = models.ForeignKey("job_type", on_delete=models.CASCADE),
=======
    job_type = models.ForeignKey("job_type", on_delete=models.CASCADE)
>>>>>>> Stashed changes
    commision_rate = models.FloatField()
    
    def calculate_income(self):
        employee_income = self.commision_rate*self.total_amount
        weekly_employee_income = employee_income*7
        monthly_employee_income = employee_income * 30
        income+=employee_income
        company_income= total_amount = employee_income
        weekly_company_income = company_income * 7
        company_income+=company_income
        
    
    
    def __str__(self):
        return self.name
    

class Employee(models.Model):
    name = models.CharField(max_length=255)
    total_amount = models.FloatField()

    def calculate_commission(self, period):
        if period == 'daily':
            commission_rate = 0.35
        elif period == 'weekly':
            commission_rate = 0.35 * 7
        elif period == 'monthly':
            commission_rate = 0.35 * 30
            

        commission = self.total_amount * commission_rate
        return commission

    def remaining_amount(self, period):
        commission = self.calculate_commission(period)
        remaining_amount = self.total_amount - commission
        return remaining_amount

class Transaction(models.Model):
    ACCOUNT_TYPES = (
        ('ASSETS', 'Assets'),
        ('LIABILITIES', 'Liabilities'),
        ('EQUITY', 'Equity'),
        ('REVENUE', 'Revenue'),
        ('EXPENSE', 'Expense'),
    )

    account = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=1000, choices=ACCOUNT_TYPES)

class commision_rate (models.Model):
   rate = models.IntegerField()

   

class commission_templates(models.Model):
    pass
