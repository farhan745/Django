from django.shortcuts import render,redirect
from django.contrib import messages
from .models import BookStore
from .forms import BookForm
# Create your views here.
def book_list(request):
    books = BookStore.objects.all()
    context = {'books': books}
    return render(request, 'all_books.html', context)
def create_book(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book created successfully!")
            return redirect('book-list')
    context = {'form': form}
    
    return render(request, 'store_book.html', context)
def update_book(request, id):
    book = BookStore.objects.get(id=id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        messages.success(request, "Book Updated successfully!")
        return redirect('book-list')
    context = {'form': form}
    return render(request, 'store_book.html', context)
def delete_book(request, id):
    book = BookStore.objects.get( id=id)

    if request.method == "POST":
        book.delete()
        messages.success(request, "Book deleted successfully!")
        return redirect('book-list')

    return render(request, "delete.html", {"book": book})
