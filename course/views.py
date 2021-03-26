from course.models import Course,Video
from course.serializers import CourseModelSerializer, VideoModelSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.
def home_page(request):
    return render(request,'Pages/home_page.html',{})

@api_view(['GET'])
# @authentication_classes([IsAuthenticated])
def course_list(request):
    qs = Course.objects.all()
    serial = CourseModelSerializer(qs,many=True)
    return Response(serial.data,status=200)


@api_view(['GET'])
# @authentication_classes([IsAuthenticated])
def video_list(request):
    qs = Video.objects.all()
    serial = VideoModelSerializer(qs,many=True)
    return Response(serial.data,status=200)

@api_view(['POST'])
@authentication_classes([IsAuthenticated])
def create_course(request):
    data = request.data or None
    serializer = CourseModelSerializer(data=data)
    if serializer.is_valid():
        obj = serializer.save(user=request.user)
        return Response(serializer.data,status=201)
    return Response({},status=400)