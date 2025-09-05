from django.http import HttpResponse
from django.shortcuts import render,redirect
from . import models

# Create your views here.
def profile(request):
    user_data = {
        'name': 'John Doe',
        'age': 17,
        'city': 'New York',
        'country': 'USA',
        
    }
    marks=[
        {
            'subject':'Math',
            'marks':90
            
        },
        {
            'subject':'English',
            'marks':85
        },
        {
            'subject':'Science',
            'marks':95
        },
        {
            'subject':'History',
            'marks':80
        } ,
        {
            'subject':'Geography',
            'marks':78
        },
        {
            'subject':'Computer Science',
            'marks':67
        }
        
    ]
    student_data = models.Student.objects.all() 
    
    
    return render(request,"student/profile.html",{
        'user': user_data,
        'marks': marks,
        'student_data': student_data
    })
def delete_student(request,id):
    student = models.Student.objects.get(id=id)
    student.delete()
    return redirect("student_profile")
    
def home(request):
    return HttpResponse("This is a home page")

