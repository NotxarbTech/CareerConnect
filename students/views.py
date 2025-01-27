from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from employers.models import JobPosting

def index(request):
    return render(request, 'students/index.html')

@login_required
def view_job_postings(request):
    all_postings = JobPosting.objects.all()
    approved_postings = []
    for posting in all_postings:
        if posting.admin_approved == True:
            approved_postings.append(posting)

    return render(request, 'students/viewjobs.html', {'job_postings': approved_postings})
