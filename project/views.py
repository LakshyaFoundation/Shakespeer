from django.shortcuts import render
from project.models import Project
from django.contrib import messages
from django.http import Http404,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def create_project(request):
	return render(request,'create.html')

def show_project(request):
	p=Project.objects.all()
	for item in p:
		item.pledge1=(item.money_req-item.pledge1)/1000
		item.pledge2=(item.money_req-item.pledge2)/100
		item.pledge3=(item.money_req-item.pledge3)/100
		item.pledge4=(item.money_req-item.pledge4)/100
	return render(request,'project.html',{'project':p})

def save_project(request):
	if request.method=="POST":
		project=Project.objects.create_project(request.POST['project_name'],request.POST['project_desc'],request.POST['money_req'],request.POST['days_req'])
		project.img_link=request.POST['img_link']
		project.details=request.POST['details']
		project.project_use=request.POST['project_use']
		project.pledge1=request.POST['pledge1']
		project.pledge2=request.POST['pledge2']
		project.pledge3=request.POST['pledge3']
		project.pledge4=request.POST['pledge4']
		project.userid=request.session['member_id']
		project.save()
		messages.info(request,'Project has been successfully created')
		return HttpResponseRedirect('/project')
