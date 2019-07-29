from django.db import models
from django.utils import timezone

# Create your models here.

class users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    Fname = models.CharField(max_length=100)
    Lname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='users')

    def __str__(self):
        return self.username


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
    def __str__(self):
        return self.full_name



    


