from django.urls import path
from .views import (
    home_page,
    course_list, pages,
    video_list,
    create_course,
    add_video_course,
    video_course_list,
    course_details,
    video_details,
    delete_video,
    delete_course,
    form_page
    )

app_name = 'course'
urlpatterns = [
    path('courses',course_list),
    path('create/course',create_course),
    path('create/course/<int:course_id>/video',add_video_course),
    path('course/<int:course_id>/video',video_course_list),
    path('course/<int:course_id>',course_details),
    path('videos',video_list),
    path('video/<int:video_id>',video_details),
    path('delete/course/<int:course_id>',delete_course),
    path('delete/video/<video_id>',delete_video),
    path('course/<int:course_id>/video/form', form_page),
    path('/sample',home_page),
    path('',pages)
]