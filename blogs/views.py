from django.shortcuts import render, redirect
from .models import *

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            user = CustomUser.objects.create(first_name=first_name,
                                            last_name=last_name, 
                                            email=email.lower())
            user.set_password(password)
            user.save()
        else:
            raise ValueError("Password and confirm_password must be same.")
        return redirect("/register/")
    return render(request, 'register.html')
        

def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if not CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Invalid Email")
            return redirect("/login/")
        
        user = authenticate(email=email, password=password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect("/login/")
        else:
            login(user)
            return redirect("/")
        
        return redirect("/login/")
    return render(request, 'login.html')