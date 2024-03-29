from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='users')
    booking= models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


Clinics = (('Dintistry','Dintistry'), ('Pediatrics','Pediatrics'), ('Dermatology','Dermatology'), ('General Medicine','General Medicine'), ('Surgery','Surgery'), ('Physical Therapy', 'Physical Therapy'), ('Neurologists','Neurologists'), ('Other','Other'))
Hospitals= (('King Faisal Hospital', 'King Faisal Hospital'), ('King Fahad Hospital','King Fahad Hospital'), ('King Khaled Hospital','King Khaled Hospital'), ('King Saud Hospital', 'King Saud Hospital'))
Genders = (('Male', 'Male'), ('Female','Female'))
Cities = (('Riyadh','Riyadh'), ('Jeddah','Jeddah'), ('Dammam','Dammam'))
Ratings= (('1','1'),('2','2'),('3','3'),('4','4'),('5','5'))

class doctors(models.Model):
    full_name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    clinic = models.CharField(max_length=100 , choices=Clinics, default='Other')
    Hospital = models.CharField(max_length=100, choices=Hospitals, default='King Saud Hospital')
    phone = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100, choices=Genders, default='Male')
    City = models.CharField(max_length=100, choices=Cities, default='Riyadh')
    picture = models.ImageField(upload_to='doctors')
    rating = models.CharField(max_length=100, choices=Ratings, default='0')
    from_date = models.DateTimeField(default=timezone.now, null=True)
    to_date = models.DateTimeField(default=timezone.now, null=True)

    
    def __str__(self):
        return self.full_name

class contact(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    user_text = models.CharField(max_length=10000)

    def __str__(self):
        return self.user_name

class appointment(models.Model):
    username = models.CharField(max_length=100)
    date = models.CharField(max_length=100)

    def __str__(self):
        return self.username