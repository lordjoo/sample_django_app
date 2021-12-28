from django.shortcuts import render
from django.conf.urls import include
from django.contrib import admin
from django.urls import path

def index(request):
    return render(request,"index.html")

urlpatterns = [
    path("",index),
    path("blog", include("posts.urls")),
    path("users", include("user.urls")),
    path('admin/', admin.site.urls),
]
