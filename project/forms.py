from django import forms
from django.forms import widgets
from django.forms import ModelForm
from project.models import Project
from django.contrib.auth.models import User

class ProjectForm(ModelForm):
	
  class Meta:
    model = Project
    exclude = ("user",)