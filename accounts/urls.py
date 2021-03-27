from django.urls import path
from accounts.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from coursecompanion import settings

app_name='accounts'
urlpatterns = [
    path('login', login_view),
    path('logout', logout_view),
    path('register', reg_view),
    path('', home_page),
    path('dashboard', dashboard),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()