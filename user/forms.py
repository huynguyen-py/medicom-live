from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField


class MyLoginForm(AuthenticationForm):
    class Meta:
        models = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(MyLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'input-field'
        self.fields['username'].widget.attrs['required'] = 'True'
        self.fields['username'].widget.attrs['placeholder'] = 'User Id...'
        self.fields['password'].widget.attrs['class'] = 'input-field'
        self.fields['password'].widget.attrs['required'] = 'True'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter Password...'


class RegisterForm(UserCreationForm):
    # email = forms.EmailFields(required=True,widget= forms.EmailInput(attrs={'required': True}))
    class Meta:
        model = User
        fields = {'username', 'email', 'dob', 'password1', 'password2'}
        fields_classes = {'username': UsernameField}
        widget = {
            'email': forms.EmailInput(attrs={'required': True})
        }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'input-field'
        self.fields['username'].widget.attrs['required'] = 'True'
        self.fields['username'].widget.attrs['placeholder'] = 'User Id...'

        self.fields['email'].widget.attrs['class'] = 'input-field'
        self.fields['email'].widget.attrs['placeholder'] = 'Email...'

        self.fields['password1'].widget.attrs['class'] = 'input-field'
        self.fields['password1'].widget.attrs['required'] = 'True'
        self.fields['password1'].widget.attrs['placeholder'] = 'Type password...'

        self.fields['password2'].widget.attrs['class'] = 'input-field'
        self.fields['password2'].widget.attrs['required'] = 'True'
        self.fields['password2'].widget.attrs['placeholder'] = 'Retype password...'

        self.fields['dob'].widget.attrs['class'] = 'input-field'
        self.fields['dob'].widget.attrs['required'] = 'True'
        self.fields['dob'].widget.attrs['type'] = 'datetime-local'

