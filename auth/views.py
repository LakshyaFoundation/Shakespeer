from django.shortcuts import render

# Create your views here.
def login(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
	return render(request,'index.html')