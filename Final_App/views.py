from django.shortcuts import render
from django.http import HttpResponse
# from .forms import 
from django.http import HttpResponseRedirect
from django.contrib import messages
# from .models import

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')   
# Create your views here.
