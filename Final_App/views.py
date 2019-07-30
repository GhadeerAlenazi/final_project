from django.shortcuts import render, reverse
from django.http import HttpResponse
from .forms import signup_form, LoginForm, ProfileForm, contactForm, DoctorProfile
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
from .models import Profile, doctors
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home_english(request):
    return render(request, 'home_English.html')

def about(request):
    return render(request, 'about.html')   

def contactus(request):
    form = contactForm()

    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form = form.save(commit=True)
           

    data={
        'form' : form
    }

    return render(request, 'contactUs.html', data)  

def Dprofile(request):
    Profile =  doctors.objects.all()

    data = {
        'profile' : Profile
    }
    return render(request, 'doctorprofile.html', data)

   

def home_arabic(request):
    return render(request, 'homeArabic.html') 

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home_english'))
def login_user(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username =username, password = password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('home_english'))

                else:
                    messages.error(request, 'user in not active')
            else:
                messages.error(request, 'invalid username or password')
    data = {
        "form_login": form
    }
    return render(request, 'login.html', data)  

# def search(request, major, clinic, Hospital, Gender, City):
def search(request):
     
     form = DoctorProfile()

     if request.method == 'POST':
        form = DoctorProfile(request.POST)
        if form.is_valid():

            clinic = form.cleaned_data['clinic']
            Hospital = form.cleaned_data['Hospital']
            Gender = form.cleaned_data['Gender']
            City = form.cleaned_data['City']

            item = form.save(commit=False)
            
    
            search_result(request, clinic, Hospital, Gender, City)

     data = {
        "form_search": form,
        
    }
     return render(request, 'search.html', data) 

def search_result(request, clinic, Hospital, Gender, City):
    try:
 
        form = doctors.objects.filter(clinic__icontains=clinic,
            Hospital__icontains=Hospital,
            Gender__icontains=Gender,
            City__icontains=City,
        )
        

    except:
        raise Http404()
    
    data = {
        "form_search_result": form
    }
    return render(request, 'result_search.html', data) 

def thanks(request):

    messages.success(request, 'Thank you for Registration')

    return render(request, 'thanks.html') 

def signup(request):
    form = signup_form()
    profileform = ProfileForm()
    if request.method == 'POST':
        form = signup_form(request.POST)
        profileform = ProfileForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            if 'picture' in request.FILES:
                item.picture = request.FILES['picture']
                item.set_password(item.password)
                item.save()

                puser = form.save(commit=False)
                puser.user = item
                puser.save()
                item.save()
                return HttpResponseRedirect('/thanks/')

    data = {
        'form_signup': form,
        'form_profile': profileform
    }
    return render(request, 'signup.html', data)  

def Uprofile(request):
    return render(request, 'userprofile.html')  
# Create your views here.
