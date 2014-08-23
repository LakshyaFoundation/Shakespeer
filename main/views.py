from django.shortcuts import render

# Create your views here.
def login(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
	return render(request,'login/index.html')
def index():
	return render('index.html')