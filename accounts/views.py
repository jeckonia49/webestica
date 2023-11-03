from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class LoginView(TemplateView):
    template_name = "accounts/authentication/login.html"

class RegisterView(TemplateView):
    template_name = "accounts/authentication/register.html"


class OtpView(TemplateView):
    template_name = "accounts/authentication/otp.html"

class ProfileView(TemplateView):
    template_name = "accounts/profile.html"
