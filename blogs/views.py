from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def register(request):
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
        

def login():
    pass