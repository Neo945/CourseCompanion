from django.urls import path
from accounts.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name='accounts'
urlpatterns = [
    path('login', login_view),
    path('logout', logout_view),
    path('register', reg_view),
    path('', home_page),
]

urlpatterns += staticfiles_urlpatterns()