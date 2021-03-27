from accounts.models import Profile
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/user/dashboard')
    form = AuthenticationForm(request,data=request.POST or None)
    if form.is_valid():
        user_ = form.get_user()
        login(request,user_)
        return redirect('/user/dashboard')
    return render(request,'accounts/login.html', {"form":form,"button":"Login"})


def reg_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        u = form.save(commit=True)
        k = False if request.POST.get('proff')=='False' else True
        data = Profile(user=u,proff=k)
        data.save()
        return redirect('/user/login')
    return render(request,'accounts/register.html', {"form":form,"button":"Register"})




def logout_view(request):
    logout(request)
    return redirect('/user/login')

def home_page(request):
    return render(request, 'accounts/home_page.html', {})

def dashboard(request):
    return render(request, 'accounts/dashboard.html',{'name':''})

def courses(request):
    return render(request, 'accounts/courses.html')

def dashboardadmin(request):
    return render(request, 'accounts/dashboardadmin.html',{'name':''})

def video_view(request):
    return render(request, 'accounts/videoviewer.html', {})