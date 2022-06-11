from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.shortcuts import render,redirect,get_object_or_404
# from .forms import CreateUserForm,ProfileForm,UpdateUserForm,ImageForm,CommentForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
# from .models import Profile,Image,Comment,Follow
# Create your views here.


def index(request):
    
    return render(request, 'index.html')

def register(request):
    # form=CreateUserForm

    # if request.method =='POST':
    #     form= CreateUserForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request,("registration successful"))
        
    #         return redirect('login')

    return render(request,'registration/register.html')

def login_in(request):
    # if request.method =='POST':
    #     username=request.POST.get('username')
    #     password=request.POST.get('password')
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         messages.success(request,("login successful"))
    #         return redirect('home')
        
    # context={}
    return render(request,'registration/login.html')

def log_out(request):
    logout(request)
    return render(request,'registration/login.html')