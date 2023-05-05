from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from brookwoodapp.models import Log
from brookwoodapp import models
# Create your views here.


def admin_dashboard(request):
    return render(request,'Admin_dashboard.html')

def admin_view_users(request):
    return render(request,'users.html')

def admin_view_complaint_report(request):
        return render(request,'view_complaints_and_reply.html')

def admin_view_bill_report(request):
    return render(request,'bill_report.html')

def admin_view_feedback(request):
    return render(request,'view_feedback.html')    

def admin_add_product(request):
    return render(request,'add_product.html')

def admin_view_product(request):
    return render(request,'view_product.html')

def admin_login(request):
    return render(request,'page-login.html')

def login_admin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        print(user)

        if user is not None and username=="admin" and password=="admn":
            login(request,user)
            return render(request,'Admin_dashboard.html')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('admin_login')
                
    else:
        return render(request, 'page-login.html')