from accounts.serializers import EnrollCreateSerializer, EnrollSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from accounts.models import Enroll, Profile
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from rest_framework.response import Response
from course.models import Course,Video


def login_view(request):
    if request.user.is_authenticated:
        if Profile.objects.filter(user=request.user).first().proff:
            return redirect('/user/dashboardadmin')
        else:
            return redirect('/user/dashboard')
    form = AuthenticationForm(request,data=request.POST or None)
    if form.is_valid():
        user_ = form.get_user()
        login(request,user_)
        if Profile.objects.filter(user=user_).first().proff:
            return redirect('/user/dashboardadmin')
        else:
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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def enrolled_courses_list(request):
    qs = Enroll.objects.filter(user=Profile.objects.filter(user= request.user).first())
    serial = EnrollSerializer(qs,many=True)
    data = serial.data
    for i in data:
        i['prof'] = Course.objects.filter(pk=i['course']).first().user.user.username
        if Video.objects.filter(course=i['course']).exists():
            i['video'] = Video.objects.filter(course=i['course']).order_by('id').first().id
        else:
            i['video'] = 0
        temp = i['course']
        i['course'] = Course.objects.filter(pk=temp).first().name
        i['course_id'] = temp
    return Response(serial.data,status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def enroll_courses(request):
    serial = EnrollCreateSerializer(data=request.data or None)
    
    if serial.is_valid():
        if Enroll.objects.filter(course=serial.validated_data['course']).exists():
            return Response({"message":"Already exists"},status=201)
        serial.save(user=Profile.objects.filter(user=request.user).first())
        return Response(serial.data,status=200)
    return Response({},status=400)


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

def video_view(request,course_id,video_id):
    return render(request, 'accounts/videoviewer.html', {})