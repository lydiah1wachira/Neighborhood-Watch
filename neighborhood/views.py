from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse ,HttpResponseRedirect, Http404
from .forms import *
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.


@login_required(login_url = 'login')
def index(request):
    '''Index view function to display the index page and all of its data'''
    
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user  = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form':form})

@login_required
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required
def EditProfile(request,username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user = user)
    form = EditProfileForm(instance=profile)
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = user
            data.hood = profile.hood
            data.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            form = EditProfileForm(instance=profile)
    legend = 'Edit Profile'
    return render(request, 'profile.html', {'legend':legend, 'form':EditProfileForm})

@login_required(login_url='login')
def create_profile(request):
    current_user = request.user
    title = "Create Profile"
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            profile = form.save()
            profile.user = current_user
            profile.save()
        return redirect('hood')

    else:
        form = CreateProfileForm()
    return render(request, 'create_profile.html', {"form": CreateProfileForm, "title": title})     

@login_required(login_url='login')
def hood(request):
    '''View function to display all the neighborhoods'''
    neighbourhoods = Neighbourhood.objects.all()
    return render(request, 'hood.html', {'neighbourhoods':neighbourhoods} )



@login_required(login_url='login')
def estate(request, id):
    neighbourhoods = Neighbourhood.objects.get(id =id)
  
    hood = Neighbourhood.objects.get(id =id)
    business = Business.objects.get(id=id)

    context = {'hood': hood, 'neighbourhoods':neighbourhoods, "business":business}
    return render(request, 'eachhood.html', context)

def search(request):
    try:
        if 'business' in request.GET and request.GET['business']:
            search_term = request.GET.get('business')
            searched_business = Business.objects.get(name__icontains=search_term)
            return render(request,'search.html',{'searched_business':searched_business})
    except (ValueError,Business.DoesNotExist):
        message = "Oops! We couldn't find the business you're looking for."
        return render(request,'search.html',{'message':message})
    return render(request,'search.html',{'message':message,'searched_business':searched_business})



        
       
     
    