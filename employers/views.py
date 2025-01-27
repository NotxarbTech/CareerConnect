from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import JobPostingForm
from .models import JobPosting

def index(request):
    return render(request, 'employers/index.html')


@login_required
def create_job_posting(request):
    # Check if the request is POST or GET and complete the necessary actions
    if request.method == 'POST':
        form = JobPostingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employers:index')
    else:
        form = JobPostingForm()
    return render(request, 'employers/newposting.html', {'form': form})


# Read more page (custom to each posting)
@login_required
def job_read_more(request, pk):
    job = get_object_or_404(JobPosting, pk=pk)
    return render(request, 'jobs/readmore.html', {'job':job})


# Application handling (either takes the user to the URL provided or allows the user to upload their resume)
@login_required
def job_apply(request, pk):
    job = get_object_or_404(JobPosting, pk=pk)
    # TODO: Job application logic
    return render(request, 'jobs/apply.html', {'job':job})

