from django import forms
from .models import Profile, doctors, User, contact


class ProfileForm(forms.ModelForm):
    picture = forms.ImageField(required = False)

    class Meta:
        model = Profile
        fields = ['firstname','lastname','phone', 'picture']

class signup_form(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)
    # email = forms.CharField(widget = forms.EmailInput)
     
    class Meta:
        model = User
        fields = ['username','email' ,'password']

class LoginForm(forms.Form):

    username = forms.CharField(max_length = 100)
    password = forms.CharField(widget = forms.PasswordInput)

class DoctorProfile(forms.ModelForm):
    # av_date = forms.CharField(
    #     widget=forms.DateTimeInput(attrs={
    #         # 'class': 'form-control datetimepicker-input',
    #         'type': 'date'
    #     })
    # )
    class Meta: 
        model = doctors
        fields = ['clinic','Hospital','Gender','City']

class contactForm(forms.ModelForm):
    user_name = forms.CharField(label = 'Your Name')
    user_email = forms.CharField(label = 'Email')
    user_text = forms.CharField(label = 'Message')
    class Meta: 
        model = contact
        fields = '__all__'


