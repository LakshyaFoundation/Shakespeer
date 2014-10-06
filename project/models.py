from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
	project_id=models.AutoField(primary_key=True)
	"""docstring for Project"""
	name=models.CharField(max_length=200)
	desc=models.CharField(max_length=400)
	money_req=models.IntegerField(default=0)
	days_req=models.IntegerField(default=0)
	photo=models.ImageField(upload_to='media/images/')
	video_link=models.URLField(max_length=1000)
	details=models.TextField(max_length=4000)
	project_use=models.CharField(max_length=100)
	pledge1=models.IntegerField(default=1)
	pledge2=models.IntegerField(default=1)
	pledge3=models.IntegerField(default=1)
	pledge4=models.IntegerField(default=1)
	date=models.DateTimeField(auto_now_add=True)
	user=models.ForeignKey(User)

class Pledgers(models.Model):
	pid=models.AutoField(primary_key=True)
	pledger=models.ForeignKey(User,related_name='pledger_user_id')
	project=models.ForeignKey(Project,related_name='pledge_project_id')
	amount_pledged=models.IntegerField(default=0)

class Document(models.Model):
	docFile=models.FileField(upload_to='project_images/')