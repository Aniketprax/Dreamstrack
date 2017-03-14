from __future__ import unicode_literals

from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=500)
    city = models.CharField(max_length=10)
    state =models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=16)
    phno = models.CharField(max_length=10)
    college = models.CharField(max_length=20, blank=True)
    school = models.CharField(max_length=20, blank=True)
    sex = models.CharField(max_length=6)
    age = models.IntegerField()


    def __str__(self):
        return self.name
