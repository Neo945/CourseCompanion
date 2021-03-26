from course.models import Course,Video
from course.serializers import CourseModelSerializer, VideoModelSerializer,CourseCreateModelSerializer,VideoCreateModelSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.
def home_page(request):
    return render(request,'Pages/home_page.html',{})

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




@api_view(['GET'])
@permission_classes([IsAuthenticated])
def video_course_list(request,course_id):
    qs = Video.objects.filter(course=course_id)
    if qs.exists():
        serial = VideoModelSerializer(qs,many=True)
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
        data['course'] = CourseModelSerializer(Course.objects.filter(pk=data['course']).first()).data['name']
        return Response(data,status=200)
    return Response({"message":"course do not exist"},status=404)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_course(request):
    u = request.user
    data = CourseCreateModelSerializer(data=request.data or None)
    if data.is_valid():
        data.save(user=u)
        print(data.data)
        return Response(data.data,status=201)
    return Response({},status=400)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_video_course(request,course_id):
    print(course_id)
    u = request.user
    data = VideoCreateModelSerializer(data=request.data or None)
    if data.is_valid():
        qs = Course.objects.filter(pk=course_id)
        if qs.exists():
            data.save(course=qs.first())
            print(data.data)
            return Response(data.data,status=201)
        return Response({"message":"course do not exist"},status=404)
    return Response({},status=400)


@api_view(['POST','GET','DELETE'])
@permission_classes([IsAuthenticated])
def delete_video(request,video_id):
    qs = Video.objects.filter(pk=video_id)
    if qs.exists():
        qs = qs.first()
        if Course.objects.filter(pk=qs.course.id).first().user == request.user:
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
        if qs.user == request.user:
            qs.delete()
            return Response({'message':'success'},status=201)
        return Response({},status=403)
    return Response({},status=404)