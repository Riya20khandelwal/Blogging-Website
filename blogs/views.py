from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout 
from .forms import RegisterForm, LoginForm, BlogForm,EditUserForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .models import *
import random
from django.core.mail import EmailMessage, send_mail


# Create your views here.

@login_required(login_url='login/')
def index(request):
    # data = Blog.objects.all()
    # print(data, "22222222222222")
    # return render(request, 'homeBlog.html', {'data':data})
    return render(request, 'homeBlog.html')


# Function to generate OTP
def generate_otp():
    return str(random.randint(100000, 999999))

# Register view
def user_signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Generate OTP
            otp = generate_otp()
            # Send OTP to user's email
            send_mail(
                'OTP for registration',
                f'Your OTP for registration is: {otp}',
                'sender@example.com',
                [email],
                fail_silently=False,
            )
            # Store email and form data in session
            request.session['email'] = email
            request.session['otp'] = otp
            request.session['form_data'] = form.cleaned_data
            # Redirect to OTP verification page
            return redirect('verify_otp')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


# Verify OTP view
def verify_otp(request):
    if request.method == 'POST':
        otp_entered = request.POST.get('otp')
        email = request.session.get('email')  # Retrieve email from session
        otp_sent = request.session.get('otp')
        if otp_entered == otp_sent:
            # If OTP matches, proceed with registration
            form = RegisterForm(request.session['form_data'])
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            # If OTP doesn't match, show error message
            return HttpResponse("Invalid OTP. Please try again.")
    else:
        # If request method is GET, render the OTP page
        return render(request, 'verify_otp.html')


# login page
@never_cache
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)    
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            # return redirect('blog_detail', blog_id=blog.id)  # Redirect to the detail view of the created blog post
            return HttpResponse("OKKK")
    else:
        form = BlogForm()
    return render(request, 'create_blog.html', {'form': form})


@login_required
def edit_user_details(request):
    user = request.user
    if request.method == 'POST':
        form = EditUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the user's profile page after saving
    else:
        form = EditUserForm(instance=user)
    return render(request, 'edit_profile.html', {'form': form})

@never_cache
@login_required(login_url='login/')
def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})

@never_cache
@login_required(login_url='login/')
def blog_detail(request, blog_id):
    blog = Blog.objects.filter(id=blog_id).first()
    print(blog.title, 77777777)
    return render(request, 'blog_detail.html', {'blog':blog})


@never_cache
@login_required(login_url='login/')
def user_logout(request):
    logout(request)
    return redirect('login')


