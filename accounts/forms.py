from collections.abc import Mapping
from typing import Any
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms.utils import ErrorList
from .models import Account


class FormSetting(forms.Form):
    def __init__(self,  *args, **kwargs):
        super(FormSetting, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Account
        fields = ("email",)

class LoginForm(FormSetting):
    class Meta:
        fields = ['email', 'password']

    widgets = {
        "email": forms.EmailInput(attrs={"placeholder":"Email Address", "id": "exampleInputEmail1"}),
        "password": forms.PasswordInput(attrs={"placeholder":"Password", "id": "exampleInputPassword1"})
    }

