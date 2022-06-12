from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Profile,Project,Comment,Ratings
# Create your views here.


def index(request):
    
    return render(request, 'index.html')

def register(request):
    form=RegisterUserForm

    if request.method =='POST':
        form= RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,("registration successful"))
        
            return redirect('login')
    context={'form':form}

    return render(request,'registration/register.html',context)

def login_in(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,("login successful"))
            return redirect('profile')
        
    context={}
    return render(request,'registration/login.html')

def log_out(request):
    logout(request)
    return render(request,'registration/login.html')

@login_required(login_url='login')
def profile(request):
    profiles=Profile.objects.get(user=request.user)
    projects=Project.objects.filter(user=request.user)

             
    context={
        'project':projects,
        'profiles':profiles, 
        }
    
    return render(request,'profile.html',context )

@login_required(login_url='login')
def update_profile(request):
    profiles = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        prof_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if  prof_form.is_valid():
            prof_form.save()
            return redirect('profile')
       
    else:
        
        prof_form = UpdateProfileForm(instance=request.user.profile)
             
    context={
      
        'prof_form': prof_form,
        
        }
    
    return render(request, 'update_profile.html',context)

@login_required(login_url='login')
def upload_project(request):
    current_user = request.user
    projects = Project.objects.all()
    profiles = Profile.get_profile()
    for profile in profiles:
        if profile.user.id == current_user.id:
            if request.method == 'POST':
                form = UploadProjectForm(request.POST,request.FILES)
                if form.is_valid():
                    new_project = form.save(commit=False)
                    new_project.user = current_user
                    new_project.profile = profile
                    new_project.save()
                    return redirect('home')
            else:
                form = UploadProjectForm()
                
            context = {
                'user':current_user,
                'form':form,
                'projects':projects,
            }
            return render(request,'upload_project.html', context)



    # projects = Project.objects.all()
    # users = User.objects.exclude(id=request.user.id)
    # if request.method == 'POST':
    #     form = UploadProjectForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.user = request.user.profile
    #         post.save()
    #         return redirect('index')
    # else:
    #     form = UploadProjectForm()
    # context = {
    #     'projects': projects,
    #     'form': form,
    #     'users': users,
    # }
    # return render(request, 'upload_project.html',context)



