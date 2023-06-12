from django.urls import path,include
from . import mathViews
from . import views
from . import payslipViews
from . import balancesheetViews
from . import employeesViews
from . import expensesViews
from . import overtimeViews
from . import dailyrecordViews
from . import departmentViews
from . import awardViews
from . import uploadViews
from . mathViews import calculate_salary


urlpatterns = [
    path('',views.index, name='index'),
    path('addemployee/', employeesViews.addEmployee, name='addEmployee'),
    path('removeemployee/', employeesViews.removeEmployee , name='removeEmployee'),
    path('employees/create/', employeesViews.addEmployee, name='employee_create'),
    path('employees/<int:pk>/', employeesViews.employee_detail, name='employee_detail'),
    path('employees/<int:pk>/update/',employeesViews. employee_update, name='employee_update'),
    path('employees/<int:pk>/delete/', employeesViews.employee_delete, name='.employee_delete'),
    path('employeeList/', employeesViews.employeeList, name='employeeList'),
    path('employeeaward/', views.employeeAward, name='employeeAward'),
    path('salarytemplates/',views.salaryTemplates, name='salaryTemplates'),
    path('commisiontemplates/', views.commisionTemplates, name='commisionTemplates' ),
    path('managesalary/', views.manageSalary , name='manageSalary'),
    path('employeeSalaryList', views.employeeSalaryList, name='employeeSalaryList'),
    path('makepayment/', views.makePayment, name = 'makePayment'),
    path('payslip/', payslipViews.generate_payslip, name='generate_payslip'),
    path('payrollsummary/', views.payrollSummary, name='payrollSummary'),
    path('advanceSalary/', views.advanceSalary, name='advanceSalary'),
    path('providentfund/', views.providentFund, name='providentFund'),
    path('overtime/', overtimeViews.overtime, name='overtime'),
    path('overtime_list/', overtimeViews.overtime_list, name='overtime_list'),
    path('create/', overtimeViews.overtime_create, name='overtime_create'),
    path('update/<int:pk>/', overtimeViews.overtime_update, name='overtime_update'),
    path('delete/<int:pk>/', overtimeViews.overtime_delete, name='overtime_delete'),
    path('award_list/', awardViews.award_list, name='award_list'),
    path('create/', awardViews.award_create, name='award_create'),
    path('update/<int:pk>/', awardViews.award_update, name='award_update'),
    path('delete/<int:pk>/', awardViews.award_delete, name='award_delete'),
    path('addDepartment/', departmentViews.addDepartment.as_view(), name='addDepartment'),
    path('removedepartment/<int:pk>/', departmentViews.removeDepartment, name='removeDepartment'),
    path('manageDepartments/', departmentViews.manageDepartments, name='manageDepartments'), 
    path('departmentlist/', departmentViews.departmentList, name='departmentList'),
    path('dailyreports/', views.dailyReports, name='dailyReports'),
    path('monthlyReports/', views.monthlyReports, name='monthlyReports'),
    path('yearlyReport/', views.yearlyReports, name='yearlyReports'),
    path('addExpenses/', views.addExpenses , name='addExpenses'),
    path('balanceSheet/', balancesheetViews.balance_sheet,name='balanceSheet'),
    path('profile/', views.profile, name='profile'),
    path('expensesList/', expensesViews.expensesList, name='expensesList'),
    path('create/', expensesViews.expense_create, name='expense_create'),
    path('update/<int:pk>/', expensesViews.expense_update, name='expense_update'),
    path('delete/<int:pk>/', expensesViews.expense_delete, name='expense_delete'),
    path('commisionList/', views.commisionList, name="commisionList"),
    path('makepaymentlist/', views.makePaymentList, name="makePaymentList"),
    path('manageSalaryList/', views.manageSalaryList, name="manageSalaryList"),
    path('dailyRecord/', dailyrecordViews.dailyRecord , name = "dailyRecord"),
    path('dailyworks/', dailyrecordViews.dailyRecordList, name='dailywork_list'),
    path('dailyworks/create/', dailyrecordViews.dailyRecord , name='dailywork_create'),
    path('dailyworks/<int:pk>/', dailyrecordViews.dailywork_detail, name='dailywork_detail'),
    path('dailyworks/<int:pk>/update/', dailyrecordViews.dailywork_update, name='dailywork_update'),
    path('dailyworks/<int:pk>/delete/', dailyrecordViews.dailywork_delete, name='dailywork_delete'),
    path('needhelp/', views.needHelp, name="needHelp"),
    path('settings/', views.settings, name= "settings"),
    path('logout/', views.sign_out, name='logout'),
    path('generatePayslip/', payslipViews.generatePayslip, name="generatePayslip"),
    path('searchexpenses/', views.search_bar, name = "search_bar")    
]

