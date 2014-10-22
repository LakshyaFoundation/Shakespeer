from django.shortcuts import render,render_to_response
from project.models import Project,Pledgers,Document
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
	return render(request,'create.html',{'form':form},context_instance=RequestContext(request))

def category(request,id):
	if request.method=="POST":
		pass

def show_project_page(request,id):
	title=''
	current_page='projects'
	projects=Project.objects.filter(project_id=id).select_related()
	current_date=timezone.make_aware(datetime.datetime.now(),timezone.get_default_timezone())
	for item in projects:
		pledgers=Pledgers.objects.filter(project_id=item.project_id).count()
		item.backers=pledgers
		title=item.name+str(' @ Crowd Fund | Lakshya Foundation')
		pledger=Pledgers.objects.filter(project_id=item.project_id ).aggregate(Sum('amount_pledged'))
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
	return render(request,'projectpage.html',{'project':projects,'title':title,'current_page':current_page})

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
	category=Project.objects.values_list('project_use', flat=True).distinct()
	return render(request,'project_1.html',{'title':title,'current_page':current_page,'project':projects,'category':category})

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

def save_project(request,**kwargs):
	if request.method == 'POST':
		user=request.user
		form = ProjectForm(request.POST, request.FILES)
		print form.is_valid()
		print form.errors
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
		pledge=Pledgers()
		pledge.pledger=request.user
		pledge.project=project
		pledge.amount_pledged=amount
		pledge.save()
		messages.info(request,'Your pledge has been recorded')
		return HttpResponseRedirect('/project/show/'+str(proj_id))


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docFile = request.FILES['docFile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('project.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )
"""
    		# print "hello"
    		# project = Project()
    		# project.photo = request.FILES['photo']
    		# project.name=request.POST['name']
    		# project.desc=request.POST['desc']
    		# project.money_req=request.POST['money_req']
    		# project.days_req=request.POST['days_req']
    		# project.details=request.POST['details']
    		# project.project_use=request.POST['project_use']
    		# project.video_link=request.POST['video_link']
    		# project.pledge1=request.POST['pledge1']
    		# project.pledge2=request.POST['pledge2']
    		# project.pledge3=request.POST['pledge3']
    		# project.pledge4=request.POST['pledge4']
    		# project.user=request.user
    		# project.save()
"""