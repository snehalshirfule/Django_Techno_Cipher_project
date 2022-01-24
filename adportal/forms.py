from django import forms
from django.forms import fields
from adportal.models import AdportalModel,AddCategoryModel,SubCategoryModel
class AdportalForm(forms.ModelForm):
    class Meta:
        model = AdportalModel
        fields = "__all__"

class SignupForm(forms.ModelForm):
    class Meta:
        model = AdportalModel
        fields = ["email","password","mobile","username",]

class SigninForm(forms.ModelForm):
    class Meta:
        model = AdportalModel
        fields = ["email","password"]

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = AddCategoryModel
        fields = ["name","describe","create_date"]

class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategoryModel
        fields = ["subname","desc","subdate"]