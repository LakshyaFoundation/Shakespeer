from django.db import models

# Create your models here.
class ProjectManager(models.Manager):
	def create_project(self,name,desc,money,days,):
		project=self.create(project_name=name,project_desc=desc,money_req=money,days_req=days)
		return project

class Project(models.Model):
	"""docstring for Project"""
	project_name=models.CharField(max_length=200)
	project_desc=models.CharField(max_length=100)
	money_req=models.IntegerField(default=1)
	days_req=models.IntegerField(default=1)
	img_link=models.CharField(max_length=1000)
	details=models.CharField(max_length=4000)
	project_use=models.CharField(max_length=100)
	pledge1=models.IntegerField(default=1)
	pledge2=models.IntegerField(default=1)
	pledge3=models.IntegerField(default=1)
	pledge4=models.IntegerField(default=1)
	pledgers=models.IntegerField(default=0)
	userid=models.IntegerField(default=0)
	objects = ProjectManager()