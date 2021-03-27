from rest_framework.serializers import ModelSerializer
from .models import Enroll
from rest_framework import serializers


class EnrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enroll
        fields = ['id','user','course','is_completed']

class EnrollCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enroll
        fields = ['course']
     

