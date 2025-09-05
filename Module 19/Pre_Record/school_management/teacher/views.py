from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'teacher/index.html',{'x':20,'num':range(2,10,2)})