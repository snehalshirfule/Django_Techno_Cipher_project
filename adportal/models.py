from tkinter import CASCADE
from django.db import models


# Create your models here.
class AdportalModel(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    mobile = models.BigIntegerField()
    password = models.CharField(max_length=50)

    class Meta:
        db_table = "adportal"

class AddCategoryModel(models.Model):
    name = models.CharField(max_length=40)
    describe = models.CharField(max_length=300)
    create_date = models.CharField(max_length=30)
    
    class Meta:
        db_table = "categorytb"


class SubCategoryModel(models.Model):
    subname = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    subdate = models.CharField(max_length=30)
    categorytb = models.ForeignKey(AddCategoryModel,on_delete= models.CASCADE)

    class Meta:
        db_table = "subcategorytb"