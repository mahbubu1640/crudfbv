from app.models import Employee
from django import forms

class EmployeeForm(forms.ModelForm): # it is a model form / it belongs to model 
    class Meta:
        model = Employee
        fields = "__all__"

from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password',]