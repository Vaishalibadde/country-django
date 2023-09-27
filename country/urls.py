from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',home),
    path('post/',post),
    path('put/<id>/', put),
    path('patch/<id>/',patch),
    path('delete/<id>/',delete)
]
