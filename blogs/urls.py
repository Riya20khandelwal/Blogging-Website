from django.urls import path
from .views import *

urlpatterns = [
    path('register/', user_signup, name='register'),
    path('login/', user_login, name='login'),
    path('', index, name='index'),
    path('logout/', user_logout, name='logout'),
    path('verify_otp/', verify_otp, name='verify_otp'),
    path('create_blog', create_blog, name='create_blog'),
    path("blog_list", blog_list, name="blog_list"),
    path('blog/<int:blog_id>/', blog_detail, name='blog_detail'),
    path('edit_user_details/', edit_user_details, name='edit_user_details'),

]