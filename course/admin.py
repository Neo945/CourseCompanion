from django.contrib import admin
from .models import Video
from .models import Course

# Register your models here.
admin.site.register(Video)
admin.site.register(Course)