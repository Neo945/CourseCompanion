from django.urls import path
from .views import (
    # home_page,
    all_ref, course_list, delete_video_ref, pages, proff_course,
    video_list,
    create_course,
    add_video_course,
    video_course_list,
    course_details,
    video_details,
    delete_video,
    delete_course,
    form_page,
    Course_video_details,
    video_ref,
    create_video_ref,
    all_ref_vid
    )

app_name = 'course'
urlpatterns = [
    path('course',course_list),
    path('video',video_list),
    path('course/create',create_course),
    path('create/course/<int:course_id>/video',add_video_course),
    path('form/course/<int:course_id>/video',form_page),
    path('course/<int:course_id>',course_details),
    path('pages/course/<int:course_id>/video',Course_video_details),
    path('course/<int:course_id>/video',video_course_list),
    path('video/<int:video_id>',video_details),
    path('delete/video/<int:video_id>',delete_video),
    path('delete/course/<int:course_id>',delete_course),
    path('video/ref/<int:video_id>',video_ref),
    path('ref',all_ref),
    path('course/<int:course_id>/video/<int:video_id>/create',create_video_ref),
    path('vide/<int:video_id>/ref',all_ref_vid),
    path('course/<int:course_id>/video/<int:video_id>/delete/<int:ref_id>',delete_video_ref),
    path('course/proff',proff_course),

    # path('/sample',home_page),
    path('',pages)
]

"""
course list
video list
create Course
video upload 
add video to course
Course_video_details
delete_course
video_course_list
proff_course
delete_video
all_ref
video_ref
{
    "name": "Django"
}

{
"name":"file.txt",
"file":"file.txt",
"type_of":"article"
}
"""