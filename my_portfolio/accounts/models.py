from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    code_link = models.TextField(null=True, blank=True)
    other_link = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.name

class Experience(models.Model):
    organization = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    start_date = models.DateField(null = True,blank = True)
    end_date = models.DateField(null = True,blank = True)
    code_link = models.TextField(null=True, blank=True)
    other_link = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.organization