from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Student
from .forms import StudentForm   # ✅ Import directly


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)  # ✅ Correct usage
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Student added successfully!")
            return redirect('student_list')
    else:
        form = StudentForm()  # ✅ Initialize empty form for GET request
    return render(request, 'student_form.html', {'form': form,'edit':True})
def student_update(request, id):
    student = get_object_or_404(Student,id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "✏️ Student updated successfully!")
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        messages.success(request, "🗑️ Student deleted successfully!")
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'student_details.html', {'student': student})
