from django.shortcuts import render,render_to_response
from project.models import Project,Pledger,ProjectUpdate
from django.contrib import messages
from django.http import Http404,HttpResponseRedirect,HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.db.models import Sum
import datetime
from django.utils import timezone
from django.template import RequestContext
from django.core.urlresolvers import reverse
from project.forms import ProjectForm,UpdateForm
import json,re
# Create your views here.
def create_project(request):
	form = ProjectForm() # A empty, unbound form
	return render(request,'project/create.html',{'form':form},context_instance=RequestContext(request))

def category(request,id):
	if request.method=="POST":
		pass

def show_project_page(request,id):
	title=''
	current_page='projects'
	projects=Project.objects.filter(project_id=id).select_related()
	current_date=timezone.make_aware(datetime.datetime.now(),timezone.get_default_timezone())
	for item in projects:
		if item.user==request.user:
			item.is_uploader=True
		pledgers=Pledger.objects.filter(project_id=item.project_id).count()
		updates=ProjectUpdate.objects.filter(project_id=id).select_related()
		for update_item in updates:
			item.update=update_item.content
		item.backers=pledgers
		title=item.name #+str(' @ Crowd Fund | Lakshya Foundation')
		pledger=Pledger.objects.filter(project_id=item.project_id ).aggregate(Sum('amount_pledged'))
		item.backer=len(pledger)
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
		# decoded_pledge_values=json.loads(item.pledge_value)
		# decoded_pledge_rewards=json.loads(item.pledge_reward)
		# item.pledge_values=decoded_pledge_values
		# item.pledge_rewards=decoded_pledge_rewards
		# item.pledge=zip(item.pledge_values,item.pledge_rewards)
		pledgers=Pledger.objects.filter(project_id=item.project_id)
		for row in pledgers:
			if row.pledger==request.user:
				item.is_pledger=True
	return render(request,'project/projectpage.html',{'project':projects,'title':title,'current_page':current_page})

def show_project(request):
	title='Projects'
	current_page='projects'
	current_date=timezone.make_aware(datetime.datetime.now(),timezone.get_default_timezone())
	projects=Project.objects.all().select_related()
	for item in projects:
		pledger=Pledger.objects.filter(project_id=item.project_id ).aggregate(Sum('amount_pledged'))
		for key,value in pledger.iteritems():
			if not value is None:
				item.percent=int(100*(float(value)/float(item.money_req)))
				item.amount_pledged=value
			else:
				item.percent=0
				item.amount_pledged=0
		diff=current_date-item.date
		if item.days_req-diff.days>0:
			item.days_left=item.days_req-diff.days
		else:
			item.days_elapsed=diff.days-item.days_req
	category=Project.objects.values_list('project_use', flat=True).distinct()
	return render(request,'project/project_1.html',{'title':title,'current_page':current_page,'project':projects,'category':category})

def pledge(request):
	if request.method=="POST":
		amount=int(request.POST.get('amount',False))
		proj_id=int(request.POST.get('pid',False))
		pledger_id=int(request.POST.get('uid',False))
		pledge=Pledger.objects.pledge(pledger_id,proj_id,amount)
		pledge.save()
		messages.info(request,'Your pledge has been recorded')
		return HttpResponseRedirect('/project')

def save_project(request,**kwargs):
	if request.method == 'POST':
		user=request.user
		form = ProjectForm(request.POST, request.FILES)
		print form.is_valid()
		print form.errors
    	if form.is_valid():
    		project=form.save(commit=False)
    		project.user=user
    		link=project.video_link
    		video_code=re.findall(r'v\=([\-\w]+)', link )[0]
    		project.video_link="//www.youtube.com/v/"+str(video_code)
    		project.save()
    		messages.info(request,'Project has been successfully created')
    		return HttpResponseRedirect('/project')
    	else:
         	raise Http404

def _pledge(request):
	if request.method=="POST":
		proj_id=int(request.POST.get('pid',False))
		amount=int(request.POST.get('amount',False))
		proj=Project.objects.filter(project_id=proj_id)
		project=Project()
		for item in proj:
			project=item
		pledge=Pledger()
		pledge.pledger=request.user
		pledge.project=project
		pledge.amount_pledged=amount
		pledge.save()
		messages.info(request,'Your pledge has been recorded')
		return HttpResponseRedirect('/project/show/'+str(proj_id))

def update_pledge(request):
	if request.method == "POST":
		proj_id=int(request.POST.get('pid',False))
		amount = int(request.POST.get('amount',False))
		proj = Project.objects.filter(project_id=proj_id)
		project = Project()
		for item in proj:
			project=item
		pledge = Pledger()
		pled = Pledger.objects.filter(project=project,pledger=request.user)
		for item in pled:
			pledge = item
		pledge.amount_pledged = amount;
		pledge.save()
		messages.info(request,'Your pledge has been updated')
		return HttpResponseRedirect('/project/show/'+str(proj_id))

def update_project(request):
	projects=Project.objects.filter(user=request.user)
	return render(request,"project/project_updates.html",{'projects':projects})
def get_update_content(request):
	if request.method=="POST":
		pid=request.POST.get('proj')
		updates=ProjectUpdate.objects.filter(project_id=pid).select_related()
		print pid
		content=""
		for update in updates:
			content=update.content
		response_data = {}
		response_data['result'] = content
		response_data['message'] = "right in the eye"
		return HttpResponse(json.dumps(response_data), content_type="application/json")
	else:
		print "not post"

def save_project_update(request):
	if request.method=="POST":
		content = request.POST.get('content')
		pid = request.POST.get('project')

		proj = Project.objects.filter(project_id=pid).select_related()
		project=Project()
		for item in proj:
			project=item
		check_project_update=ProjectUpdate.objects.filter(project_id=project)
		update=ProjectUpdate()
		if check_project_update:
			for item in check_project_update:
				update=item
			update.content=content
			update.save()
			messages.info(request,'Project Update has been successfully added')
		else:
			update.content=content
			update.project_id=project
			update.save()
			messages.info(request,'Project Update has been successfully added')
    	return HttpResponseRedirect('/project')
