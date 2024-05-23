from django.urls import path
from .views import *

urlpatterns = [
    path('register/', user_signup, name='register'),
    path('login/', user_login, name='login'),
    path('', index, name='index'),
    path('logout/', user_logout, name='logout'),
    path('verify_otp/', verify_otp, name='verify_otp'),

]