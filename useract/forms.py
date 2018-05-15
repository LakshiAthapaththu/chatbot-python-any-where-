from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from useract.models import ProfilePic

class SignUpForm(UserCreationForm):
    picture = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

#just check
class ImageForm(ModelForm):
    class Meta:
        model=ProfilePic
        fields = ['picture']

class editProfile(ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(),required=False,min_length=8)
    new_password = forms.CharField(widget=forms.PasswordInput(),required=False,min_length=8)
    current_password = forms.CharField(widget=forms.PasswordInput(),required=True,
                                 help_text="You need to enter your current password")
    username = forms.CharField(min_length=1,max_length=255,required=False)
    #if user name is taken from User model it becomes a required field
    #newly added fields
    class Meta:
        model=User
        fields = ['username','first_name','last_name','email']
        #fields extended from user model



