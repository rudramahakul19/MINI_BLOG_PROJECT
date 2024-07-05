from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post
from .forms import SignUpForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
# Create your views here.

# Home
def HOME(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts':posts})

# About
def ABOUT(request):
    return render(request, 'blog/about.html')


# Contact
def CONTACT(request):
    return render(request, 'blog/contact.html')


# Dashboard
def DASHBOARD(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()

        # Profile show side bar
        user = request.user
        full_name = user.get_full_name()
        group = user.groups.all()
        return render(request, 'blog/dashboard.html', {'posts':posts, 'full_name':full_name, 'group':group})
    else:
        return HttpResponseRedirect('/login/')


# User_Logout
def USER_LOGOUT(request):
    logout(request)
    return HttpResponseRedirect('/')


# User_SignUP
def SIGN_UP(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            group = Group.objects.get(name = 'Auther')
            user.groups.add(group)
            messages.success(request, 'Congratulations ! You have become an auther')
            
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form':form})


# User_login
def USER_LOGIN(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request, data = request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']

                user=authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully !!')
                    return HttpResponseRedirect('/dashboard/')
               
        else:
            form = LoginForm()
        return render(request, 'blog/login.html', {'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')
    

# Add New Post
def ADD_POST(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                post = Post(title=title, desc=desc)
                post.save()
                messages.success(request, 'Post added successfully !!')
                form =PostForm()
        else:
            form =PostForm()
        return render(request, 'blog/addpost.html', {'form':form})
    
    else:
        return HttpResponseRedirect('/login/')
    


# Update Post
def UPDATE_POST(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            post_id = Post.objects.get(pk = id)
            form = PostForm(request.POST, instance=post_id)
            if form.is_valid():
                form.save()
                messages.success(request, 'Post updated successfully !!')
                return HttpResponseRedirect('/dashboard/')
        else:
            post_id = Post.objects.get(pk = id)
            form = PostForm(instance=post_id)
        return render(request, 'blog/updatepost.html', {'form':form})
    else:
        return HttpResponseRedirect('/login/')
    

# Delete Post
def DELETE_POST(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            post_id = Post.objects.get(pk = id)
            post_id.delete()
        return HttpResponseRedirect('/dashboard/')
    
    else:
        return HttpResponseRedirect('/login/')