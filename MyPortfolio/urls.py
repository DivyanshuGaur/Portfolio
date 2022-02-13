
from django import views
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

        path('',views.index,name="index"),
        path('/divyanshu/projects',views.projects,name="projects"),
        path('/divyanshu/resume',views.resume,name="resume"),
        path('/divyanshu/achivements',views.achive,name="achive")


    
] + static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
