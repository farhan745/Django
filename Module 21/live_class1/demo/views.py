from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def data(request):
    person = "John Doe"
    return render(request,'index.html',{'name':person})
def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def reports(request):
    return render(request,'reports.html')
