from django.urls import path
from accounts.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name='accounts'
urlpatterns = [
    path('login', login_view),
    path('logout', logout_view),
    path('register', reg_view),
    path('', home_page),
    path('courses', dashboard),
    path('enrolled',enrolled_courses_list),
    path('create/enroll',enroll_courses),
    path('dashboard', courses),
    path('dashboard1', dashboard1),
    path('dashboardadmin', dashboardadmin),
    path('course/<int:course_id>/videos/<int:video_id>', video_view)
    
]

urlpatterns += staticfiles_urlpatterns()