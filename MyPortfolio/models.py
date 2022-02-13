from django.db import models

# Create your models here.


class Project(models.Model):
    title=models.CharField(max_length=30)
    desc=models.CharField(max_length=100)
    tags=models.CharField(max_length=30)
    img=models.ImageField(upload_to="uploads",null=True)
    link=models.CharField(max_length=300,null=True)


    def __str__(self) -> str:
        return self.title


class Achivements(models.Model):
        ac=models.CharField(max_length=500)
        link=models.CharField(max_length=400,null=True,blank=True)
        lt=models.CharField(max_length=500,null=True,blank=True)



class Resume(models.Model):
    img=models.ImageField(upload_to="uploads")







