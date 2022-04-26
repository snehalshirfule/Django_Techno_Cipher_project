from django.db import models
from django.db.models.fields import BigIntegerField

# Create your models here.
class VendorModel(models.Model):
    username = models.CharField(max_length=30)
    email_ID = models.EmailField()
    mobile_no = models.BigIntegerField()
    password = models.CharField(max_length=50)
    shop_name = models.CharField(max_length=50)
    owner_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6,blank=True)
    address = models.CharField(max_length=150)
    business_desc = models.CharField(max_length=250)
    gst_no = models.CharField(max_length=50)
    executive_ID = models.CharField(max_length=50)
    image_profile = models.CharField(max_length=250)

    class Meta:
        db_table = "vendor"

class Image(models.Model):
    photo = models.ImageField(upload_to="myimage")
    date = models.DateTimeField(auto_now_add=True)


