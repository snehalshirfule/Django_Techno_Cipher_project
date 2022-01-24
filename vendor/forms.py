from django import forms
from django.forms import fields
from vendor.models import VendorModel
class VendorForm(forms.ModelForm):
    class Meta:
        model = VendorModel
        fields = "__all__"

class Registration_Form(forms.ModelForm):
    class Meta:
        model = VendorModel
        fields = ["username","email_ID","mobile_no","password"]

class AuthForm(forms.ModelForm):
    class Meta:
        model = VendorModel
        fields = ['email_ID','password']

class DashForm(forms.ModelForm):
    class Meta:
        model = VendorModel
        fields = ['shop_name','owner_name','city','pincode','address','business_desc','gst_no','executive_ID','image_profile']