from django.http import request
from django.shortcuts import render
from .models import Project,Resume,Achivements

# Create your views here.


def index(request):

    return render(request,'MyPortfolio/index.html')


def projects(request):
    projects=Project.objects.all()
  
    return render(request,'MyPortfolio/projects.html',{"proj_data":projects})


def resume(request):
    res=Resume.objects.all()
    print(res[0].img.url)
    return render(request,'MyPortfolio/resume.html',{'r':res[0]})


def achive(request):
    ac=Achivements.objects.all()
    return render(request,'MyPortfolio/achive.html',{'ac':ac})