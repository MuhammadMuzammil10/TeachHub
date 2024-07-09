from django.shortcuts import render, redirect
from .models import JobDescription
from .filter_logic import scan_job_description



def home(request):
    jobs = JobDescription.objects.all()
    return render(request, 'filter_app/home.html', {'jobs': jobs})


def submit_job(request):
    if request.method == 'POST':
        content = request.POST['content']
        is_flagged = scan_job_description(content)
        status = 'Rejected' if is_flagged else 'Approved'
        job = JobDescription(content=content, status=status)
        job.save()
        return redirect('home')
    return render(request, 'filter_app/submit_job.html')

