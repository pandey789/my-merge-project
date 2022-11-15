from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm 
from .models import User
from .models import Post
from django import forms
#from django.contrib.auth import get_user_model



class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("username", "email")

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)


    class Meta:
        model = User
        fields = ("username", "password")

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        # model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'description']      

    
    




