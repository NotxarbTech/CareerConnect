from django.urls import path

from . import views

# Registers the app name
app_name = "students"

urlpatterns = [
    path("", views.index, name="index"),
    path("jobs/", views.view_job_postings, name="view_jobs")
]