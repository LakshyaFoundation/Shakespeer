from django.shortcuts import render,render_to_response
from project.models import Project,Pledger,ProjectUpdates
from django.contrib import messages
from django.http import Http404,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.db.models import Sum
import datetime
from django.utils import timezone
from django.template import RequestContext
from django.core.urlresolvers import reverse
from project.forms import ProjectForm

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
		pledgers=Pledger.objects.filter(project_id=item.project_id).count()
		updates=ProjectUpdates.objects.filter(project_id=id).select_related()
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
	category=Project.objects.values_list('project_use', flat=True).distinct()
	return render(request,'project/project_1.html',{'title':title,'current_page':current_page,'project':projects,'category':category})

def pledge(request):
	if request.method=="POST":
		amount=int(request.POST.get('amount',False))
		proj_id=int(request.POST.get('pid',False))
		pledger_id=int(request.POST.get('uid',False))
		print pledger_id
		pledge=Pledger.objects.pledge(pledger_id,proj_id,amount)
		pledge.save()
		messages.info(request,'Your pledge has been recorded')
		return HttpResponseRedirect('/project')

def save_project(request,**kwargs):
	if request.method == 'POST':
		user=request.user
		form = ProjectForm(request.POST, request.FILES)
		# print form.is_valid()
		# print form.errors
    	if form.is_valid():
    		project=form.save(commit=False)
    		project.user=user
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
			print type(item)
		pledge=Pledger()
		pledge.pledger=request.user
		pledge.project=project
		pledge.amount_pledged=amount
		pledge.save()
		messages.info(request,'Your pledge has been recorded')
		return HttpResponseRedirect('/project/show/'+str(proj_id))
def list(request):
	pass