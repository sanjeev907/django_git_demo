from django.shortcuts import render,HttpResponse
from . models import department,Role,Employee
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
    return render (request,"index.html") 

def all_emp(request):
    emp=Employee.objects.all()
    data={
        'emp':emp
    }
    print(data)
    return render (request,"ViewAll_emp.html",data) 


def add_emp(request):
   if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        new_emp = Employee(first_name= first_name, last_name=last_name, salary=salary, bonus=bonus, Phone=phone, dept_id = dept, role_id = role, hire_date = datetime.now())
        new_emp.save()
        return HttpResponse('Employee added Successfully')
   elif request.method=='GET':
        return render(request, 'add_emp.html')
   else:
        return HttpResponse("An Exception Occured! Employee Has Not Been Added")



def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_remove = Employee.objects.get(id=emp_id)
            emp_to_be_remove.delete()
            return HttpResponse("Employee removed Successfully")
        except:
            return HttpResponse("Please Enter the Vaild EMP. ID")

    else:
        emp=Employee.objects.all()
        data1={
            'emp':emp
        }
        return render (request,"remove_emp.html",data1) 



def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)

        data2 = {
            'emps': emps
        }
        return render(request, 'ViewAll_emp.html',data2)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')
    