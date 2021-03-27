from accounts.models import Profile
from course.models import Course, Reference,Video
from course.serializers import (
    CourseModelSerializer, RefernceSerializer, 
    VideoModelSerializer,
    CourseCreateModelSerializer,
    VideoCreateModelSerializer,
    RefernceCreateSerializer
    )
from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .firebases import firebase_download,firebase_upload,firebase_delete

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def form_page(request,course_id):
    qs = Course.objects.filter(pk=course_id)
    if qs.exists():
        if qs.first().user.user == request.user:
            serial = CourseModelSerializer(qs.first())
            return render(request,'Pages/form.html',{"course":serial.data})
        return render(request=request,status=403)
    return render(request=request,status=404)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Course_video_details(request,course_id):
    qs = Course.objects.filter(pk=course_id)
    if qs.exists():
        if qs.first().user.user == request.user:
            serial = CourseModelSerializer(qs.first())
            return render(request,'Pages/video_list.html',{"course":serial.data})
        return render(request=request,status=403)
    return render(request=request,status=404)
# def home_page(request):
#     return render(request,'Pages/form.html',{})

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def course_list(request):
    qs = Course.objects.all()
    serial = CourseModelSerializer(qs,many=True)
    return Response(serial.data,status=200)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def video_list(request):
    qs = Video.objects.all()
    serial = VideoModelSerializer(qs,many=True)
    return Response(serial.data,status=200)

def pages(request):
    return render(request,"Pages/home_page.html",{})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def video_course_list(request,course_id):
    qs = Video.objects.filter(course=course_id)
    if qs.exists():
        serial = VideoModelSerializer(qs,many=True)
        data = serial.data
        for i in serial.data:
            i['course'] = i['video'].split('/')[0] #CourseModelSerializer(Course.objects.filter(pk=(i['course'])).first()).data['name']
            # k = i['course'] + '/' + i['video']
            i['video'] = firebase_download(i['video'])
            print(i['video'])
        return Response(serial.data,status=200)
    return Response({"message":"course do not exist"},status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def course_details(request,course_id):
    qs = Course.objects.filter(pk=course_id)
    if qs.exists():
        serial = CourseModelSerializer(qs.first())
        data = {"course":serial.data}
        videos = Video.objects.filter(course=course_id)
        data['videos'] = videos.count()
        print(data)
        return Response(data,status=200)
    return Response({"message":"course do not exist"},status=404)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def video_details(request,video_id):
    qs = Video.objects.filter(pk=video_id)
    if qs.exists():
        serial = VideoModelSerializer(qs.first())
        data = serial.data
        data['course'] = data['video'].split('/')[0] #CourseModelSerializer(Course.objects.filter(pk=data['course']).first()).data['name']
        # k = data['course'] + '/' + data['video']
        data['video'] = firebase_download(data['video'])
        print(data['video'])
        return Response(data,status=200)
    return Response({"message":"course do not exist"},status=404)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_course(request):
    u = request.user
    data = CourseCreateModelSerializer(data=request.data or None)
    if data.is_valid():
        if Profile.objects.filter(user=u).first().proff:
            data.save(user=Profile.objects.filter(user=u).first())
            print(data.data)
            return Response(data.data,status=201)
        return Response({},status=403)
    return Response({},status=400)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_video_course(request,course_id):
    data = VideoCreateModelSerializer(data=request.data or None)
    if data.is_valid():
        qs = Course.objects.filter(pk=course_id)
        print(qs)
        if qs.exists() and qs.first().user.proff:
            data.save(course=qs.first())
            print(data.data)
            data = data.data
            data['course'] = qs.first().id
            return Response(data,status=201)
        return Response({"message":"course do not exist"},status=404)
    return Response({},status=400)


@api_view(['POST','GET','DELETE'])
@permission_classes([IsAuthenticated])
def delete_video(request,video_id):
    qs = Video.objects.filter(pk=video_id)
    if qs.exists():
        qs = qs.first()
        if Course.objects.filter(pk=qs.course.id).first().user.user == request.user and Course.objects.filter(pk=qs.course.id).first().user.proff:
            firebase_delete(qs.video)
            qs.delete()
            return Response({'message':'success'},status=201)
        return Response({},status=403)
    return Response({},status=404)


@api_view(['POST','GET','DELETE'])
@permission_classes([IsAuthenticated])
def delete_course(request,course_id):
    qs = Course.objects.filter(pk=course_id)
    if qs.exists():
        qs = qs.first()
        if qs.user.user == request.user and qs.user.proff:
            # firebase_delete(qs.name)
            v = Video.objects.filter(course=qs.id)
            for i in VideoModelSerializer(v,many=True).data:
                firebase_delete(i['video'])
            qs.delete()
            return Response({'message':'success'},status=201)
        return Response({},status=403)
    return Response({},status=404)





@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_ref(request):
    qs = Reference.objects.all()
    serial = RefernceSerializer(qs,many=True)
    return Response(serial.data,status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_video_ref(request,course_id,video_id):
    u = request.user
    data = RefernceCreateSerializer(data=request.data or None)
    if data.is_valid():
        qs = Video.objects.filter(pk=video_id)
        print(qs)
        if qs.exists():
            if Course.objects.filter(pk=course_id).first().user.user == u and Course.objects.filter(pk=course_id).first().user.proff:
                data.save(video=qs.first())
                print(data.data)
                return Response(data.data,status=201)
            return Response({},status=403)
        return Response({"message":"course do not exist"},status=404)
    return Response({},status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def all_ref_vid(request,video_id):
    qs = Reference.objects.filter(video=video_id)
    serial = RefernceSerializer(qs,many=True)
    for i in serial.data:
        i['file'] = firebase_download(i['file'])
    return Response(serial.data,status=200)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def video_ref(request,video_id):
    qs = Reference.objects.filter(video=video_id)
    if qs.exists():
        serial = RefernceSerializer(qs,many=True)
        return Response(serial.data,status=200)
    return Response({},status=404)

@api_view(['POST','GET','DELETE'])
@permission_classes([IsAuthenticated])
def delete_video_ref(request,course_id,video_id,ref_id):
    qs = Reference.objects.filter(pk=ref_id)
    if qs.exists():
        qs = qs.first()
        if Course.objects.filter(pk=course_id).first().user.user == request.user and Course.objects.filter(pk=course_id).first().user.proff:
            firebase_delete(qs.file)
            qs.delete()
            return Response({'message':'success'},status=201)
        return Response({},status=403)
    return Response({},status=404)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def proff_course(request):
    prof = Profile.objects.filter(user=request.user).first()
    c = Course.objects.filter(user=prof)
    serial = CourseModelSerializer(c,many=True)
    data = serial.data
    for i in data:
        videos = Video.objects.filter(course__id=i['id'])
        i['videos'] = videos.count()
    return Response(data,status=200)