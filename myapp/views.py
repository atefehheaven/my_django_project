# myapp/views.py
from django.shortcuts import render, get_object_or_404, redirect # <-- مطمئن شو که get_object_or_404 رو هم اضافه کردی
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from .serializers import PostSerializer
from .models import Post
from .forms import PostForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') # بعد از ثبت‌نام موفق، کاربر رو به صفحه ورود میفرستیم
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def post_list(request):
    posts = Post.objects.all().order_by('-pub_date')
    return render(request, 'index.html', {'posts': posts})

def post_detail(request, post_id): # <-- این تابع باید دقیقاً همینطور تعریف شده باشه
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})

@login_required
def post_create(request):
    if request.method == 'POST':
    
        form = PostForm(request.POST) 
        if form.is_valid():
            
            form.save() 
            return redirect('post_list') 
    else:
        form = PostForm()

    return render(request, 'post_create.html', {'form': form})

@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id) 

    if request.method == 'POST':
        if form.is_valid():
            form.save() 
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post) 

    return render(request, 'post_edit.html', {'form': form, 'post': post})

@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'post_confirm_delete.html', {'post': post})

class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'id'

