from django.urls import path
from .views import (
    home_page,
    course_list,
    video_list
    )

app_name = 'course'
urlpatterns = [
    path('courses',course_list),
    path('videos',video_list),
    path('', home_page),
]