from django.urls import path
from . import views

urlpatterns = [
    path('api/jobs', views.JobList.as_view(), name='job_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/jobs/<int:pk>', views.JobDetail.as_view(), name='job_detail'), # api/contacts will be routed to the ContactDetail view for handling
]
