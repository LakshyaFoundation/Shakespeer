from django.shortcuts import render
from project.models import Project,Pledgers
from django.contrib import messages
from django.http import Http404,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.db.models import Sum
# Create your views here.
def create_project(request):
	return render(request,'create.html')

def show_project_page(request,id):
	p=Project.objects.filter(project_id=id)
	return render(request,'projectpage.html',{'project':p})

def _pledge(request):
	if request.method=="POST":
		amount=int(request.POST.get('amount',False))
		proj_id=int(request.POST.get('pid',False))
		pledger_id=int(request.POST.get('uid',False))
		print pledger_id
		pledge=Pledgers.objects.pledge(pledger_id,proj_id,amount)
		pledge.save()
		messages.info(request,'Your pledge has been recorded')
		return HttpResponseRedirect('/project')

def show_projects(request):	
	p=Project.objects.all()
	pl=Pledgers.objects.all()#values('project_id').distinct()
	res=[]
	amsum=[]
	for item in p:
		user=User.objects.filter(id=item.userid)
	for proj in pl:
		pt=Pledgers.objects.filter(project_id=proj.project_id).aggregate(Sum('amount_pledged'))
		res.append({'amount':pt['amount_pledged__sum'],'proj_id':proj.project_id})
	percent=[]
	for item in p:
		for ans in res:
			print item.project_id,' ',ans['proj_id']
			if item.project_id==ans['proj_id']:
				amsum.append(ans['amount'])
				ans['amount']=(item.money_req-ans['amount'])*100.00/item.money_req
				percent.append({'amount':ans['amount'],'proj_id':ans['proj_id']})
				print ans['amount']
	return render(request,'project.html',{'project':p,'user':user,'res':percent})

def save_project(request):
	if request.method=="POST":
		project=Project.objects.create_project(request.POST['project_name'],request.POST['project_desc'],request.POST['money_req'],request.POST['days_req'])
		project.img_link=request.POST['img_link']
		project.details=request.POST['details']
		project.project_use=request.POST['project_use']
		project.video_link=request.POST['video_link']
		project.pledge1=request.POST['pledge1']
		project.pledge2=request.POST['pledge2']
		project.pledge3=request.POST['pledge3']
		project.pledge4=request.POST['pledge4']
		project.userid=request.user.id
		project.save()
		messages.info(request,'Project has been successfully created')
		return HttpResponseRedirect('/project')
def pledge(request):
	if request.method=="POST":
		pledge=Pledgers.objects.pledge(request.user.id,request.POST['project_id'],request.POST['amount'])
		pledge.save()
		messages.info(request,'Your pledge has been recorded')
		return HttpResponseRedirect('/')