# # app - forms.py file new

# from django import forms
# from .models import CustomUser

# class UserForm(forms.ModelForm):
#     class Meta:
#         model=CustomUser
#         fields =('first_name','last_name','email','password','confirm_password')
#         # fields = '__all__'

#     # def __init__(self, *args, **kwargs):
#     #     super(UserForm, self).__init__(*args, **kwargs)
#     #     for visible in self.visible_fields():
#     #         visible.field.widget.attrs['class'] = 'form-control'

from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email',  'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

# class BlogForm(forms.Form):
#     class Meta:
#         model = Blog
#         fields = ('title', 'text' )