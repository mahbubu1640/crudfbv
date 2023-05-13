from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
#from django.models import Q
from django.db.models import Avg,Sum,Max,Min,Count 
from app.models import Employee
from django.db.models.functions import Lower
from app.forms import EmployeeForm
from django.shortcuts import redirect
from app.forms import SignupForm
def display_view(request):
    employee = Employee.objects.all()
    my_dict={'employee':employee}
    return render(request,'app/home.html',my_dict)

def create_view(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'app/create.html',{'form':form})

def delete_view(request,pk):
    employee=Employee.objects.get(pk=pk)
    employee.delete()
    return redirect('/')
    #return render(request,'app/delete.html')

def update_view(request,pk):
    employee=Employee.objects.get(pk=pk)
    form= EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'app/update.html',{'employee':employee})
# def update_view(request,id):
#     employee=Employee.objects.get(id=id)
#     if request.method=="POST":
#         form=EmployeeForm(request.POST,instance=employee)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     return render(request,'app1/update.html',{'employee':employee})

def detail_view(request,pk):
    employee=Employee.objects.get(pk=pk)
    return render(request,'app/detail.html',{'employee':employee})


def signup_view(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'app/signup.html',{'form':form})