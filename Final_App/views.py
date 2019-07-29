from django.shortcuts import render, reverse
from django.http import HttpResponse
from .forms import signup_form, LoginForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Profile, doctors
from django.contrib.auth import authenticate, login, logout

def home_english(request):
    return render(request, 'home_English.html')

def about(request):
    return render(request, 'about.html')   

def contactus(request):
    return render(request, 'contactUs.html')  

def Dprofile(request):
    return render(request, 'doctorprofile.html')  

def home_arabic(request):
    return render(request, 'homeArabic.html')  

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

def search(request):
    return render(request, 'search.html') 

def thanks(request):

    messages.success(request, 'Thank you for Registration')

    return render(request, 'thanks.html') 

def signup(request):
    form = signup_form()
    if request.method == 'POST':
        form = signup_form(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            if 'picture' in request.FILES:
                item.picture = request.FILES['picture']
            item.save()
            return HttpResponseRedirect('/thanks/')

    data = {
        'form_signup': form
    }
    return render(request, 'signup.html', data)  

def Uprofile(request):
    return render(request, 'userprofile.html')  
# Create your views here.
