from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.

def login_view(request):
    form = AuthenticationForm(request,data=request.POST or None)
    if form.is_valid():
        user_ = form.get_user()
        login(request,user_)
        return redirect('/')
    return render(request,'accounts/auth.html',{"form":form,"button":"Login"})

def reg_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        # user_ = form.get_user()
        # login(request,user_)
        print(form.cleaned_data)
        u = form.save(commit=True)
        # return redirect('/login')
    return render(request,'accounts/auth.html',{"form":form,"button":"Register"})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        redirect('/login')
    return render(request,'accounts/auth.html',{"form":None,"button":"Logout"})

def home_page(request):
    return render(request, 'accounts/home_page.html', {})