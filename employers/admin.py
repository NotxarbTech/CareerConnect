from django.contrib import admin

from .models import JobPosting

# Registering the Job Posting field in the admin tab
admin.site.register(JobPosting)