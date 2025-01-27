from django.db import models
from django.urls import reverse

# Model to store job postings to be accessed by admins, students, and employers
class JobPosting(models.Model):
    job_name = models.CharField(max_length=200)
    job_description = models.CharField(max_length=10000)
    employer_name = models.CharField(max_length=200)
    employer_phone = models.CharField(max_length=30)
    employer_email = models.CharField(max_length=100)
    minimum_age = models.IntegerField(null=True, default=None, blank=True)
    min_pay = models.IntegerField(null=True, default=None, blank=True)
    max_pay = models.IntegerField(null=True, default=None, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    application_url = models.URLField(max_length=200, null=True, default=None, blank=True)
    # TODO: Allow admin users to change from false to true
    admin_approved = models.BooleanField(default=True)

    # If accessed as a string, it will show the job name
    def __str__(self):
        return self.job_name
    
    # Return the url for the job's "read more" page
    def get_read_more_url(self):
        return reverse('employers:job_read_more', args=[self.pk])
    
    # Return the url for the job's application page, if that does not exist take the user to the CareerConnect application page
    def get_apply_url(self):
        if self.application_url is not None:
            return self.application_url
        
        return reverse('employers:job_apply', args=[self.pk])