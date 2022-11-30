from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='/profile_pics/default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} profile'
    def save(self):
        super().save()


class Users (models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=200)
    first_name = models.CharField(max_length=100,default="none")
    last_name = models.CharField(max_length=100, default="none")
    def __str__(self):
        return self.user


class demousers (models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(to=Users,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class login(models.Model):
    id = models.AutoField(primary_key=True)
    user=models.CharField(max_length=200)
    password=models.CharField(max_length=300)