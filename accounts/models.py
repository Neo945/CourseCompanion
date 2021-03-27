from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    proff = models.BooleanField(null=False,default=False)