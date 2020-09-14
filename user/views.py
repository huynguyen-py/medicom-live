from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView
from user.models import User

# Create your views here.


class AdminCvView(TemplateView):
    template_name = 'MediCom/admin_profile.html'


class SiteLoginView(LoginView):
    template_name = 'MediCom/user_login.html'


class SiteProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'MediCom/user_profile.html'


class RegisterForm(UserCreationForm):
    # email = forms.EmailFields(required=True,widget= forms.EmailInput(attrs={'required': True}))
    class Meta:
        model = User
        fields = {'username', 'email', 'address', 'phone_number', 'dob', 'passport'}
        fields_classes = {'username': UsernameField}
        widget = {
            'email': forms.EmailInput(attrs={'required': True})
        }


class SiteRegisterView(FormView):
    template_name = 'MediCom/user_register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        data = form.cleaned_data

        self.new_user = User.objects.create_user(
            username=data['username'],
            password=data['password1'],
            email=data['email'],
            address=data['address'],
            phone_number=data['phone_number'],
            dob=data['dob'],
            passport=data['passport']
        )
        self.new_user.is_staff = True
        # self.new_user.is_superuser = True
        self.new_user.is_active = True
        self.new_user.save()

        return redirect(reverse('login'))


class SiteLogoutView(LogoutView):
    template_name = 'MediCom/user_logout.html'

