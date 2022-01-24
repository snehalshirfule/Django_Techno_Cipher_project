from django.db import models

# Create your models here.
class UserModel(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    mobile = models.BigIntegerField()
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=250)

    class Meta:
        db_table = "user"