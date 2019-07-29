from django.shortcuts import render
from django.http import HttpResponse
# from .forms import 
from django.http import HttpResponseRedirect
from django.contrib import messages
# from .models import

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
    return render(request, 'login.html')  

def search(request):
    return render(request, 'search.html')  

def signup(request):
    return render(request, 'signup.html')  

def Uprofile(request):
    return render(request, 'userprofile.html')  
# Create your views here.
