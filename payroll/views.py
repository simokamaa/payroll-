from django.shortcuts import render,redirect
from .forms import *
from first.models import *
from django.views import View
from django.urls import path,include
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect


# def login(request):
#     manager = Manager.objects.all()
#     return render(request, 'index.html')

# class login(View):
#     model = Manager
#     form_class = ManagerForm
#     template_name = 'index.html'
#     success_url = 'index.html'
    
#     def get(self,request):
#         login_details = self.form_class()
#         return render(request, 'index.html')
    
#     def post(self,request):
#         login_details = self.form_class(request.POST,request.FILES)
        
#         if login_details.is_valid():
            
#             return redirect ("home")
        
#         return render(request, 'index.html')
    



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home/',username=username)  # Redirect to the admin dashboard
        else:
            error_message = 'Invalid username or password'
    else:
        error_message = None
    
    return render(request, 'index.html', {'error_message': error_message})
