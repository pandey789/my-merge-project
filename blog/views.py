from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post, User
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from . import forms
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm



def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            print(user, "uuuuuuuu")
            login(request, user)
            return redirect('post_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})

def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            return redirect('post_list')
            if user is not None:
                login(request, user)
                
                message = f'Hello {user.username}! You have been logged in'
            else:
                message = 'Login failed!'
    return render(
        request, 'blog/login.html', context={'form': form, 'message': message})

def logout_request(request):
	logout(request)
	return redirect("post_list")

@login_required
def profile(request):
    return render(request, 'blog/profile.html')





