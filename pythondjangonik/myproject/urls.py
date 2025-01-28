from django.contrib import admin
from django.urls import path, re_path, include
from myapp import views 
  

urlpatterns = [
    path("", views.index),
    re_path("about", views.about),
    re_path("contacts", views.contacts),
    re_path("forms", views.forms),
    re_path("postuser/", views.postuser),
]