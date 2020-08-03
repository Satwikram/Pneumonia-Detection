from django.contrib import admin
from django.urls import path
from detect import views
from detect.views import *

urlpatterns = [
                path('', views.predict, name = 'predict'),
]