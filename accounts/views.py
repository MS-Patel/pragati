
from django.shortcuts import render,redirect
from django.contrib import messages
from accounts.models import Register
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model
User = get_user_model()

def loginpage(request):
    
        return render(request,'login.html')

def regpage(request):
    
        return render(request,'register.html')

def register(request):
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        username   = request.POST['username']
        password   = request.POST['password']
        confirm_password = request.POST['confirm_password']
        email        = request.POST['email']

        if password==confirm_password:
            if Register.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('accounts:register')
            elif Register.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('accounts:register')
            else:   

                user = Register.objects.create(username=username, password=password,confirm_password=confirm_password, email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                messages.info(request,'Register Successfully..') 
                return redirect('accounts:loginpage')

        else:
            messages.info(request,'password not matching..')    
            return redirect('accounts:register')
        return redirect('lead:home')
        
    else:
        return render(request,'register.html')

def login_in(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = Register.objects.get(username=username)
            if user and user.password==password:
               
                return redirect('lead:home')
            else:
                messages.info(request,'invalid credentials')
                return redirect('accounts:loginpage')
        except:
            
            return render(request,'login.html')
