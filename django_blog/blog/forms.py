from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Registration Form with Email Field
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Profile Update Form
class ProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
