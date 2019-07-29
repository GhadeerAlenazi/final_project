from django import forms
from .models import Profile, doctors

class signup_form(forms.ModelForm):
    picture = forms.ImageField(required = False)
    password = forms.CharField(widget = forms.PasswordInput)
    email = forms.CharField(widget = forms.EmailInput)
     
    class Meta:
        model = Profile
        fields = ['picture', 'Username', 'First name', 'Last name', 'phone','email' ,'password']

class LoginForm(forms.Form):

    username = forms.CharField(max_length = 100)
    password = forms.CharField(widget = forms.PasswordInput)