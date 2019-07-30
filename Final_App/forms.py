from django import forms
from .models import Profile, doctors, User


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