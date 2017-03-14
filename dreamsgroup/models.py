from __future__ import unicode_literals

from django.db import models


class College(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    active = models.IntegerField()
    cover = models.CharField(max_length=500,default="img/")

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    active = models.IntegerField()
    cover = models.CharField(max_length=500,default="img/")

    def __str__(self):
        return self.name


class Events(models.Model):
    name = models.CharField(max_length=50)
    college = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


def user_directory_path(instance):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/post/%y/%m/%d/'.format(instance)


class Post(models.Model):
    user = models.IntegerField()
    userName = models.CharField(max_length=500)
    date = models.DateTimeField()
    college = models.IntegerField()
    collegeName = models.CharField(max_length=500)
    content = models.TextField(max_length=5000,blank=True)
    video = models.CharField(max_length=6000,blank=True)
    image = models.ImageField(blank=True,upload_to='post/%Y/%m/%d')
    flag = models.BooleanField(default=False)

    def __str__(self):
        return self.content
