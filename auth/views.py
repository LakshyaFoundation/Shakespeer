from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render_to_response
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def login(request):
	return render(request,'login.html')

def _login(request):
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')
    try:
        m = Member.objects.get(username=request.POST['username'])
        if m.password == request.POST['password']:
            request.session['member_id'] = m.id
            return HttpResponseRedirect('auth/login')
    except Member.DoesNotExist:
        return HttpResponse("Your username and password didn't match.")

def register(request):
	return render(request,'register.html')

def create_user(request):
	if request.method=="POST":
		username=request.POST['display_name']
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
			return render(request,'success.html')
		else:
			messages.error(request, 'Password mismatch.')
		return render(request,'login.html')
	return render(request,'login.html')
