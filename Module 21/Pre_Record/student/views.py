from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from . import forms
from django.contrib import messages
# Create your views here.

# todo: This is for HTML Forms
# def home(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         password = request.POST.get('password')
#         checkbox = request.POST.get('checkbox')
#         photo = request.FILES.get('photo')
        
#         student = models.Student(
#             name=name,
#             email=email,
#             phone=phone,
#             password=password,
#             checkbox=checkbox,
#             photo=photo
#         ) #student class er object banailam
#         if checkbox == 'on':
#             student.checkbox = True
#         else:
#             student.checkbox = False
#         student.save() #save method diye database e save korlam
#         return HttpResponse("Data saved successfully!")

#     return render(request, 'student/index.html')

# todo: This is for Model Forms
def create_student(request):
    
    if request.method=="POST": #user post request korse
        form = forms.StudentForm(request.POST, request.FILES) #user post req data req ta capture korlam
        if form.is_valid(): #form valid kina check korlam
            form.save()
            messages.success(request, "Student created successfully!") 
            return redirect('home')
    else:
        form = forms.StudentForm()
    return render(request, 'student/create_student.html', {'form':form})
def student_details(request, id):
    student= models.Student.objects.get(id=id)
    return render(request, 'student/student_details.html', {'student':student})
def update_student(request, id):
    student= models.Student.objects.get(id=id)
    form = forms.StudentForm(request.POST or None, request.FILES or None, instance=student)
    if form.is_valid():
        form.save()
        messages.success(request, "Student Updated successfully!") 
        return redirect('home')
    return render(request, 'student/create_student.html', {'form':form, 'edit':True})
def deleteStudent(request, id):
    student= models.Student.objects.get(id=id)
    student.delete()
    messages.error(request, "Student Deleted successfully!") 
    return redirect('home')

def home(request):
    students = models.Student.objects.all() #database theke sob student data niye aslam
    return render(request, 'student/index.html', {'students':students})