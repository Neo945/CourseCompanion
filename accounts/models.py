import django
from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings
from django.apps import apps

User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    proff = models.BooleanField(null=False,default=False)

class Enroll(models.Model):
    course = models.ForeignKey('course.Course',on_delete=models.CASCADE)
    user = models.ForeignKey(Profile,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False,null=False)