from django.contrib.auth.models import AbstractUser
from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class UserNet(AbstractUser):
    '''Custom user model'''
    middle_name = models.CharField(max_length=50)
    first_login = models.DateTimeField(null=True)
    phone = models.CharField(max_length=14)
    avatar = models.ImageField(upload_to='user/avatar', null=True, blank=True)
    bio = models.TextField(max_length=2000, blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    gender = models.CharField(blank=True, null=True, choices=
    (('Male', 'Male'), ('Female', 'Female'), ('Non-binary', 'Non-binary')))
    date_of_birth = models.DateField(blank=True, null=True)
    technology = models.ManyToManyField(Technology, related_name='users')
