from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Course(models.Model):
    name = models.CharField(null=False,max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # playlist = models.

def valid(value):
    if value not in ['reference book','refernce link','article']:
        raise ValidationError("Not a possible Resourse")

class Reference(models.Model):
    name = models.CharField(null=False,max_length=255)
    file = models.CharField(null=False,max_length=255)
    type_of = models.CharField(validators=[valid],max_length=20,null=False)
    video = models.ForeignKey('Video',on_delete=models.CASCADE)



class Video(models.Model):
    name = models.CharField(null=False,max_length=255)
    video = models.CharField(null=False,max_length=255)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
