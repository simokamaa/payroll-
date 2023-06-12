from django.shortcuts import render
from .models import Employees

#employees count
def employees_count(request):
    employee_count = Employees.objects.count()
    return render(request, 'Dashboard/index.html', {'employee_count' : employee_count})