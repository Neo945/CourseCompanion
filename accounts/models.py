from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings
# from course.models import Course

User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    proff = models.BooleanField(null=False,default=False)

# class Enroll(models.Model):
#     course = models.ForeignKey(Course,on_delete=models.CASCADE)
#     user = models.ForeignKey(Profile,on_delete=models.CASCADE)
#     timestamp = models.DateTimeField(auto_now_add=True)