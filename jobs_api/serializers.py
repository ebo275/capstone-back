from rest_framework import serializers 
from .models import Job 

class JobSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Job # tell django which model to use
        fields = ('id', 'title', 'company', 'salary', 'dateApplied', 'response') # tell django which fields to include
