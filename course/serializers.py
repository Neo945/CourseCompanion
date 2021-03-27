from rest_framework.serializers import ModelSerializer
from .models import Course,Video
from rest_framework import serializers
from .firebases import firebase_download

class CourseCreateModelSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['name','id']

class CourseModelSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ['name','id','user','timestamp']

class VideoModelSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = ['id','name','course','video']


class VideoCreateModelSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = ['id','name','video']