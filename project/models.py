from django.db import models
from django.contrib.auth.models import User
from main.models import IntegerRangeField
# Create your models here.

class Project(models.Model):
	project_id=models.AutoField(primary_key=True)
	"""docstring for Project"""
	name=models.CharField(max_length=200)
	desc=models.CharField(max_length=400)
	money_req=IntegerRangeField(default=0,min_value=20000,max_value=200000)
	days_req=IntegerRangeField(default=0,min_value=7,max_value=60)
	#money_req=models.IntegerField(default=1)
	#days_req=models.IntegerField(default=1)
	photo=models.ImageField(upload_to='images/')
	video_link=models.URLField(max_length=1000)
	details=models.TextField(max_length=4000)
	project_use=models.CharField(max_length=100)
	risks_and_challenges=models.TextField(max_length=4000)
	#number_of_options=models.IntegerField(default=1)
	#pledge_value=models.TextField(max_length=1000)
	#pledge_reward=models.TextField(max_length=8000)
	date=models.DateTimeField(auto_now_add=True)
	user=models.ForeignKey(User)
	def __unicode__(self):
		return str(self.name)

class Pledger(models.Model):
	pid=models.AutoField(primary_key=True)
	pledger=models.ForeignKey(User,related_name='pledger_user_id')
	project=models.ForeignKey(Project,related_name='pledge_project_id')
	amount_pledged=models.IntegerField(default=0)
	def __unicode__(self):
		return str(self.pid)+' '+str(self.pledger)+' '+str(self.project)

class ProjectUpdate(models.Model):
	id=models.AutoField(primary_key=True)
	content = models.TextField(max_length = 4000)
	date = models.DateTimeField(auto_now_add = True)
	project_id = models.ForeignKey(Project)

	def __unicode__(self):
		return str(self.project_id)