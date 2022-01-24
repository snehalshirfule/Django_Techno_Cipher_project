from django import forms
from django.forms import fields
from user.models import UserModel

class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = "__all__"

class SignupForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ["email","password","mobile","username","address"]


class SigninForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ["email","password"]

