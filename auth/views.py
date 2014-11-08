from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from project.models import Project

# Create your views here.
def __login(request):
	current_page='login'
	title="Login"
	return render(request,'auth/login.html',{'current_page':current_page,'title':title})

def _login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
		if user.is_active:
			login(request, user)
			messages.info(request,'Welcome '+user.username)
			return HttpResponseRedirect('/project')
		else:
			messages.info(request,'Your account is inactive. Contact webmaster')
			return HttpResponseRedirect('/auth/login')
    else:
		messages.error(request,'Invalid username/password')
		return HttpResponseRedirect('/auth/login')

def profile(request,uid):
	user=User.objects.filter(id=uid)
	project=Project.objects.filter(userid=uid)
	return render(request,'auth/profile.html',{'user':user,'project':project})

def _logout(request):
	logout(request)
	messages.info(request,'You have been logged out')
	print('Bye')
	return HttpResponseRedirect('/auth/login')

def register(request):
	return render(request,'auth/register.html')

def create_user(request):
	if request.method=="POST":
		username=request.POST['email']
		password=request.POST['password']
		firstname=request.POST['first_name']
		lastname=request.POST['last_name']
		email=request.POST['email']
		password=request.POST['password']
		confirm_password=request.POST['password_confirmation']
		if password == confirm_password:
			user=User.objects.create_user(firstname,email,password)
			user.last_name=lastname
			user.username=username
			user.save()
			return render(request,'auth/success.html')
		else:
			messages.error(request, 'Password mismatch.')
		return render(request,'auth/login.html')
	return render(request,'auth/login.html')
