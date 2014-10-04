from django.shortcuts import render
from project.models import Project,Pledgers
from django.contrib import messages
from django.http import Http404,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.db.models import Sum
import datetime
from django.utils import timezone
# Create your views here.
def create_project(request):
	return render(request,'create.html')

def show_project_page(request,id):
	p=Project.objects.filter(project_id=id)
	return render(request,'projectpage.html',{'project':p})

def pledge(request):
	if request.method=="POST":
		amount=int(request.POST.get('amount',False))
		proj_id=int(request.POST.get('pid',False))
		pledger_id=int(request.POST.get('uid',False))
		print pledger_id
		pledge=Pledgers.objects.pledge(pledger_id,proj_id,amount)
		pledge.save()
		messages.info(request,'Your pledge has been recorded')
		return HttpResponseRedirect('/project')

def show_project(request):
	title='Projects'
	current_page='projects'
	current_date=timezone.make_aware(datetime.datetime.now(),timezone.get_default_timezone())
	projects=Project.objects.all().select_related()
	for item in projects:
		pledger=Pledgers.objects.filter(project_id=item.project_id ).aggregate(Sum('amount_pledged'))
		for key,value in pledger.iteritems():
			if not value is None:
				item.percent=(100*(float(value)/float(item.money_req)))
				item.amount_pledged=value
			else:
				item.percent=0
				item.amount_pledged=0
		diff=current_date-item.date
		if item.days_req-diff.days>0:
			item.days_left=item.days_req-diff.days
		else:
			item.days_elapsed=diff.days-item.days_req
	return render(request,'project_1.html',{'title':title,'current_page':current_page,'project':projects})

def test(request):
	p=Project.objects.all()
	for item in p:
		item.pledge1=(item.money_req-item.pledge1)/1000
		item.pledge2=(item.money_req-item.pledge2)/100
		item.pledge3=(item.money_req-item.pledge3)/100
		item.pledge4=(item.money_req-item.pledge4)/100
	return render(request,'project.html',{'project':p})

def save_project(request):
	if request.method=="POST":
		project=Project()
		project.name=request.POST['project_name']
		project.desc=request.POST['project_desc']
		project.money_req=request.POST['money_req']
		project.days_req=request.POST['days_req']
		project.img_link=request.POST['img_link']
		project.details=request.POST['details']
		project.project_use=request.POST['project_use']
		project.video_link=request.POST['video_link']
		project.pledge1=request.POST['pledge1']
		project.pledge2=request.POST['pledge2']
		project.pledge3=request.POST['pledge3']
		project.pledge4=request.POST['pledge4']
		project.user=request.user
		project.save()
		messages.info(request,'Project has been successfully created')
		return HttpResponseRedirect('/project')

def _pledge(request):
	if request.method=="POST":
		proj_id=int(request.POST.get('pid',False))
		amount=int(request.POST.get('amount',False))
		proj=Project.objects.filter(project_id=proj_id)
		project=Project()
		for item in proj:
			project=item
			print type(item)
		pledge=Pledgers()
		pledge.pledger=request.user
		pledge.project=project
		pledge.amount_pledged=amount
		pledge.save()
		messages.info(request,'Your pledge has been recorded')
		return HttpResponseRedirect('/project/show/'+str(proj_id))