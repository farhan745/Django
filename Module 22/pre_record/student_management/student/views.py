from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
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
@login_required
def create_student(request):
    
    if request.method=="POST": #user post request korse
        form = forms.StudentForm(request.POST, request.FILES) #user post req data req ta capture korlam
        if form.is_valid(): #form valid kina check korlam
            student=form.save(commit=False) #form er data save korlam, but commit false dile database e save hobe na
            student.user = request.user  # Logged in user ke assign korlam
            student.save() #database e save korlam
            messages.success(request, "Student created successfully!") 
            return redirect('home')
    else:
        form = forms.StudentForm()
    return render(request, 'student/create_student.html', {'form':form})
@login_required
def student_details(request, id):
    student= models.Student.objects.get(id=id)
    return render(request, 'student/student_details.html', {'student':student})
@login_required
def update_student(request, id):
    student= models.Student.objects.get(id=id)
    form = forms.StudentForm(request.POST or None, request.FILES or None, instance=student)
    if form.is_valid():
        student=form.save(commit=False)# form er data save korlam, but commit false dile database e save hobe na
        student.updated_by = request.user  # Logged in user ke assign korlam
        student.save() #database e save korlam
        messages.success(request, "Student Updated successfully!") 
        return redirect('home')
    return render(request, 'student/create_student.html', {'form':form, 'edit':True})
@login_required
def deleteStudent(request, id):
    student= models.Student.objects.get(id=id)
    student.delete()
    messages.error(request, "Student Deleted successfully!") 
    return redirect('home')

def home(request):
    students = models.Student.objects.all() #database theke sob student data niye aslam
    return render(request, 'student/index.html', {'students':students})

def signup(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('home')

        
    return render(request, 'student/signup.html', {'form':form,'signup_bar':True}) 

'''def user_login(request):
    form = forms.CustomLoginForm()
    if request.method == "POST":
        form = forms.CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()   # Django নিজেই user বের করে দেয়
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect("home")
    return render(request, "student/login.html", {"form": form, "signup_bar": True})'''
#todo: Default Login with username and password
def user_login_default(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm( data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully!")
                return redirect("home")
        messages.error(request, "Invalid username or password.")
    return render(request, "student/login_default.html", {"form": form, "signup_bar": True})
    
    #todo: Login with email
def user_login_email(request):
    if request.method == "POST":
        form = forms.EmailLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email') 
            password = form.cleaned_data.get('password')

            try:
                user_obj = User.objects.get(email=email)  # email দিয়ে user খোঁজা
                user = authenticate(username=user_obj.username, password=password)
                if user is not None:
                    login(request, user)
                    #* ✅ Session এ user ID save
                    request.session['user_id'] = user.id
                    request.session['user_email'] = user.email
                    
                    messages.success(request, "✅ Logged in successfully!")  # success message
                    return redirect('home')
                else:
                    messages.error(request, "❌ Invalid password.")  # wrong password
            except User.DoesNotExist:
                messages.error(request, "❌ Email not found.")  # wrong email
        else:
            messages.error(request, "❌ Please correct the form.")  # invalid form
    else:
        form = forms.EmailLoginForm()

    return render(request, "student/login_with_email.html", {"form": form,'signup_bar':True})

def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login_email')
@login_required
def profile(request):
    students = models.Student.objects.filter(user=request.user) #database theke sob student data niye aslam
    return render(request, 'student/profile.html', {'students':students})