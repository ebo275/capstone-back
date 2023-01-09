from django.db import models

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=55)
    company = models.CharField(max_length=55)
    salary = models.IntegerField()
    dateApplied = models.CharField(max_length=55)
    response = models.BooleanField()
