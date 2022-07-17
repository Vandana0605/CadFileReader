from django.contrib import admin
from django.urls import path
from FileReaderApp import views

from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('filedetail', views.fileread, name='filedetail'),
]
