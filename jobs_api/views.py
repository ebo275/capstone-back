from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import JobSerializer
from .models import Job

class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = JobSerializer # tell django what serializer to use

class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all().order_by('id')
    serializer_class = JobSerializer
