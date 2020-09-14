from django import forms
from .models import User


class MyLoginForm(forms.ModelForm):
    class Meta:
        models = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'required': 'True', 'placeholder': 'User Id'}),
            'password': forms.TextInput(attrs={'required': 'True', 'placeholder': 'Password'})
        }
