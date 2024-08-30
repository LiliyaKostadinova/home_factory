from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')  # Add other fields as necessary
        
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
        label='Username'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        label='Password'
    )
