"""Final_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Final_App import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_english, name='home_english'),
    path('about/', views.about, name='about'),
    path('home_arabic/', views.home_arabic, name ='home_arabic'),
    path('contactus/', views.contactus, name ='contact'),
    path('login/', views.login_user, name ='login'),
    path('logout/', views.user_logout, name='logout'),
    path('search/', views.search, name ='search'),
    path('signup/', views.signup, name ='signup'),
    path('doctorprofile/', views.Dprofile, name ='doctor'),
    path('userprofile/<str:username>', views.Uprofile, name ='user'),
    path('thanks/', views.thanks, name = 'thanks'),
    path('search_result/', views.search_result, name='search_result'),
    path('booking/<int:id>', views.booking, name='booking'),
    path('save/<str:username>', views.savebooking, name='savebooking'),

    # path(r'^search_result/(?P<clinic>\w+)/(?P<Hospital>\w+)/(?P<Gender>\w+)/(?P<City>\w+)/$', views.search_result, name='search_result'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
