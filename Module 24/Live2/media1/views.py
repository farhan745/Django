from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth import login, authenticate
from . import models

# Create your views here.
@login_required
def media_list(request):
    media_files = models.MediaFile.objects.filter(user=request.user).order_by('-uploaded_at')   
    return render(request, 'media/media_list.html', {'media_files': media_files})
@login_required
def media_upload(request):
    if request.method=="POST":
        form = forms.MediaFileForm(request.POST,request.FILES)
        if form.is_valid():
            media_file = form.save(commit=False)
            media_file.user = request.user
            media_file.save()
            return redirect('media:media_list')
    else:
        form = forms.MediaFileForm()
    return render(request, 'media/media_form.html', {'form': form})

@login_required
def media_edit(request, pk):
    media_file = get_object_or_404(models.MediaFile, pk=pk, user=request.user)
    if request.method == "POST":
        form = forms.MediaFileForm(request.POST, request.FILES, instance=media_file)
        if form.is_valid():
            form.save()
            return redirect('media:media_list')
    else:
        form = forms.MediaFileForm(instance=media_file)
    return render(request, 'media/media_form.html', {'form': form})
@login_required
def media_delete(request, pk):
    media_file = get_object_or_404(models.MediaFile, pk=pk, user=request.user)
    if request.method == "POST":
        media_file.delete()
    return redirect('media:media_list')
   