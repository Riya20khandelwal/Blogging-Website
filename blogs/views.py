# # from django.shortcuts import render, redirect
# # from .models import *

# # from django.contrib.auth import authenticate, login, logout
# # from django.contrib import messages

# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout 
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.cache import never_cache
# from .models import *
# import random
# from django.core.mail import EmailMessage, send_mail
# from forms import 

# # signup page
# # @never_cache
# # def user_signup(request):
# #     if request.method == 'POST':
# #         form = RegisterForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('login')
# #     else:
# #         form = RegisterForm()
# #     return render(request, 'register.html', {'form': form})

# # Create your views here.
# def register_user(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         password = request.POST['password']
#         confirm_password = request.POST['confirm_password']

#         if password == confirm_password:
#             user = CustomUser.objects.create(first_name=first_name,
#                                             last_name=last_name, 
#                                             email=email.lower())
#             user.set_password(password)
#             user.save()
#         else:
#             raise ValueError("Password and confirm_password must be same.")
#         return redirect("/register/")
#     return render(request, 'register.html')
        

# def login_user(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']

#         if not CustomUser.objects.filter(email=email).exists():
#             messages.error(request, "Invalid Email")
#             return redirect("/login/")
        
#         user = authenticate(email=email, password=password)

#         if user is None:
#             messages.error(request, "Invalid Password")
#             return redirect("/login/")
#         else:
#             login(user)
#             return redirect("/")
        
#         return redirect("/login/")
#     return render(request, 'login.html')




# # # Create your views here.
# # # Home page
# # @login_required(login_url='login/')
# # def index(request):
# #     data = Blog.objects.all()
# #     print(data, "22222222222222")
# #     return render(request, 'homeBlog.html', {'data':data})

# # # signup page
# # @never_cache
# # def user_signup(request):
# #     if request.method == 'POST':
# #         form = RegisterForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('login')
# #     else:
# #         form = RegisterForm()
# #     return render(request, 'register.html', {'form': form})

# # # login page
# # @never_cache
# # def user_login(request):
# #     if request.method == 'POST':
# #         form = LoginForm(request.POST)
# #         print("sdfg")
# #         if form.is_valid():
# #             print("11211111111111")
# #             email = form.cleaned_data['email']
# #             password = form.cleaned_data['password']
# #             print("dfgvhb")
# #             user = authenticate(request, email=email, password=password)
# #             print("sxdcfvgbh")
# #             if user:
# #                 print("okkkkkkkkkk")
# #                 login(request, user)    
# #                 return redirect('home')
# #     else:
# #         form = LoginForm()
# #     return render(request, 'login.html', {'form': form})

# # @never_cache
# # @login_required(login_url='login/')
# # def create_blog(request):
# #     if request.method == 'POST':
# #         user= request.user
# #         blog_name = request.POST['blog_name']
# #         title = request.POST['title']
# #         category = request.POST['category']
# #         content = request.POST['content']
# #         blog_image =  request.FILES.get('blog_image')
# #         Blog(author=user,
# #              blog_name=blog_name,
# #              title=title,
# #              category=category,
# #              blog_image=blog_image,
# #              content=content).save()
# #         return redirect('home')
# #     return render(request,'createBlog.html')

# # def get_blog(request):
# #     data = Blog.objects.all()
# #     return render(request,'blog_list.html', {'data':data})

# # # logout page
# # @never_cache
# # @login_required(login_url='login/')
# # def user_logout(request):
# #     logout(request)
# #     return redirect('login')


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout 
from .forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from .models import *
import random
from django.core.mail import EmailMessage, send_mail


# Create your views here.
# Home page
@login_required(login_url='login/')
def index(request):
    # data = Blog.objects.all()
    # print(data, "22222222222222")
    # return render(request, 'homeBlog.html', {'data':data})
    return render(request, 'homeBlog.html')


# Function to generate OTP
def generate_otp():
    return str(random.randint(1000, 9999))

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


# # Register view
# def user_signup(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             # Generate OTP
#             otp = generate_otp()
#             # Send OTP to user's email
#             send_mail(
#                 'OTP for registration',
#                 f'Your OTP for registration is: {otp}',
#                 'sender@example.com',
#                 [email],
#                 fail_silently=False,
#             )
#             # Store the OTP in session for verification later
#             request.session['otp'] = otp
#             # Render a template with a form to input OTP
#             return render(request, 'verify_otp.html', {'email': email})
#     else:
#         form = RegisterForm()
#     return render(request, 'register.html', {'form': form})


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


# # Verify OTP view
# def verify_otp(request):
#     if request.method == 'POST':
#         otp_entered = request.POST.get('otp')
#         email = request.POST.get('email')
#         # Retrieve OTP from session
#         otp_sent = request.session.get('otp')
#         if otp_entered == otp_sent:
#             # If OTP matches, proceed with registration
#             form = RegisterForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('login')
#         else:
#             # If OTP doesn't match, show error message
#             return HttpResponse("Invalid OTP. Please try again.")
#     else:
#         # If request method is GET, render a template with a form to input OTP
#         email = request.GET.get('email')
#         return render(request, 'verify_otp.html', {'email': email})


# signup page
# @never_cache
# def user_signup(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             # print(form.password1,888888888)
#             # if form.password1 == form.password2:
#             form.save()
#             return redirect('login')
#             # else:
#             #     return HttpResponse("<h1> Password not same</h1>")
#     else:
#         form = RegisterForm()
#     return render(request, 'register.html', {'form': form})

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

# @never_cache
# @login_required(login_url='login/')
# def create_blog(request):
#     if request.method == 'POST':
#         user= request.user
#         blog_name = request.POST['blog_name']
#         title = request.POST['title']
#         category = request.POST['category']
#         content = request.POST['content']
#         blog_image =  request.FILES.get('blog_image')
#         Blog(author=user,
#              blog_name=blog_name,
#              title=title,
#              category=category,
#              blog_image=blog_image,
#              content=content).save()
#         return redirect('home')
#     return render(request,'createBlog.html')

# def get_blog(request):
#     data = Blog.objects.all()
#     return render(request,'blog_list.html', {'data':data})

# logout page
@never_cache
@login_required(login_url='login/')
def user_logout(request):
    logout(request)
    return redirect('login')


