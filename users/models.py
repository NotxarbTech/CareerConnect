from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # List of possible roles a user can have, includes tuples with code-friendly and human-friendly versions.
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('employer', 'Employer')
    ]
    # Field to show which role the user has, can only be selected from the roles listed above
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_approved = models.BooleanField(default=False) # Only for students
