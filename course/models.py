from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Course(models.Model):
    name = models.CharField(null=False,max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # playlist = models.

class Video(models.Model):
    name = models.CharField(null=False,max_length=255)
    # video = models.FileField(upload_to='/')
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
