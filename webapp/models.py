from django.db import models

# Create your models here.
class user(models.Model):
    user_id = models.CharField(max_length=30)
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    class Meta:
        db_table="user"

class login(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=25)
    category = models.CharField(max_length=30)
    class Meta:
        db_table="login"