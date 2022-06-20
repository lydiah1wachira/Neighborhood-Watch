from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse ,HttpResponseRedirect, Http404
from .forms import NewUserForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required



# Create your views here.
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
   
			return redirect('login/')

		messages.error(request, "Unsuccessful registration. Invalid information.")
  
	form = NewUserForm()
	return render (request, "registration/register.html", context={"register_form":form})


def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login (request, user)
            return redirect('create_profile')
        else:
            messages.info(request, 'Username Or Password is incorrect')    
    
    context = {}
    return render(request, 'registration/login.html', context)


@login_required
def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("login")


@login_required
def index(request):
    '''Index view function to display the index page and all of its data'''
    
    return render(request, 'index.html')