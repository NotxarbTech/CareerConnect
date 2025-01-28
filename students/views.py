from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
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


def search_results(request):
    query = request.GET.get('q', '')

    # Check if the user is authenticated, if not save the search query and redirect them to login
    if not request.user.is_authenticated:
        request.session['search_query'] = query
        return redirect('users:login')
    
    results = None
    if query:
        results = JobPosting.objects.filter(
            Q(job_name__icontains=query) | Q(employer_name__icontains=query)
        )

    return render(request, 'students/searchresults.html', {'query':query, 'results':results})
    
