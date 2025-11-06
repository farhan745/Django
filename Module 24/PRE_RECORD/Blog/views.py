from django.shortcuts import render,redirect,get_object_or_404
from .models import Post, Category, Tag
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from .forms import SignupForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.
@login_required
def post_list(request):
    
    posts = Post.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    tags = Tag.objects.all()

    # search query
    query = request.GET.get('q')
    if query:
        posts = posts.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    # category filter
    categoryQuery = request.GET.get('category')
    if categoryQuery:
        posts = posts.filter(category__name=categoryQuery)

    # tag filter
    tagQuery = request.GET.get('tag')
    if tagQuery:
        posts = posts.filter(tags__name=tagQuery)

    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'categories': categories,
        'tags': tags,
        'query': query,  # template এ দেখানোর জন্য
    })
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('post_list')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()  # Save the many-to-many data for the form
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})
@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_update.html', {'form': form, 'post': post})
def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_details.html', {'post': post})
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})