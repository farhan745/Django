from django.shortcuts import render
from . import models
# Create your views here.
def post_list(request):
    post = models.Post.objects.all()
    return render(request,'index.html',{'posts':post})
def post_details(request,pk):
    post = models.Post.objects.get(pk=pk)
    return render(request,'post_details.html',{'post':post})
