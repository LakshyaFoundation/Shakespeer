from django.shortcuts import render

# Create your views here.
def index(request):
	flag=False
	if request.user.is_authenticated():
		flag=True
	else:
		flag=False
	return render(request,'project.html',{'logged_in':flag})

def create(request):
	flag=False
	if request.user.is_authenticated():
		flag=True
	else:
		flag=False
	return render(request,'create.html',{'logged_in':flag})