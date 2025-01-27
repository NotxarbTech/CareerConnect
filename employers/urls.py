from django.urls import path

from . import views

# Registers the app name
app_name = "employers"

urlpatterns = [
    path("", views.index, name="index"),
    path("createposting/", views.create_job_posting, name="create_posting"),
    path("jobs/<int:pk>/read-more", views.job_read_more, name="job_read_more"),
    path("jobs/<int:pk>/apply", views.job_apply, name="job_apply"),
]