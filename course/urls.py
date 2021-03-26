from django.urls import path
from .views import (
    home_page,
    course_list,
    video_list,
    create_course
    )

app_name = 'course'
urlpatterns = [
    path('courses',course_list),
    path('create/courses',create_course),
    path('videos',video_list),
    path('', home_page),
]