from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200,null=True, blank=True,default='')
    description = models.TextField(null=True, blank=True,default='')
    thumbnail = models.TextField(null=True, blank=True,default='')
    body = models.TextField(null=True, blank=True,default='')
    code_link = models.TextField(null=True, blank=True,default='')
    other_link = models.TextField(null=True, blank=True,default='')


    def __str__(self):
        return self.name

class Experience(models.Model):
    organization = models.CharField(max_length=200,null=True, blank=True,default='')
    description = models.TextField(null=True, blank=True,default='')
    thumbnail = models.TextField(null=True, blank=True,default='')
    body = models.TextField(null=True, blank=True,default='')
    start_date = models.CharField(max_length=200,null=True, blank=True,default='')
    end_date = models.CharField(max_length=200,null=True, blank=True,default='')
    code_link = models.TextField(null=True, blank=True,default='')
    other_link = models.TextField(null=True, blank=True,default='')


    def __str__(self):
        return self.organization