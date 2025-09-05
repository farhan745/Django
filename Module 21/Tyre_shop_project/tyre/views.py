from django.shortcuts import render, redirect, get_object_or_404
from .models import Tyre
from .forms import TyreForm
from django.contrib import messages

# Public tyre list
def tyre_list(request):
    tyres = Tyre.objects.all()  # ✅ objects
    return render(request, 'tyre_list.html', {'tyres': tyres})

# Public tyre detail
def tyre_details(request, id):
    tyre = get_object_or_404(Tyre, id=id)  # ✅ safer than objects.get
    return render(request, 'tyre_details.html', {'tyre': tyre})
def tyres_admin_list(request):
    tyres = Tyre.objects.all()
    return render(request, "admin_list.html", {"tyres": tyres})
def create_tyre(request):
    form = TyreForm()
    if request.method == "POST":
        form = TyreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Tyre created successfully.")
            return redirect('tyres_admin_list')
    return render(request, 'create_tyre.html', {'form': form})
def update_tyre(request, id):
    tyre = get_object_or_404(Tyre, id=id)
    form = TyreForm(request.POST or None, request.FILES or None, instance=tyre)
    if form.is_valid():
        form.save()
        messages.info(request, "Tyre updated successfully.")
        return redirect('tyres_admin_list')
    return render(request, 'update_tyre.html', {'form': form})

def delete_tyre(request, id):
    tyre = get_object_or_404(Tyre, id=id)
    if request.method == "POST":
        tyre.delete()
        messages.error(request, "Tyre deleted successfully.")
        return redirect('tyres_admin_list')
    return render(request, 'delete_tyre.html', {'tyre': tyre})