from django.shortcuts import render, redirect
from .models import JobDescription
from .filter_logic import scan_job_description
from filter_app.forms import *


def home(request):
    jobs = JobDescription.objects.all()
    return render(request, 'filter_app/home.html', {'jobs': jobs})


def submit_job(request):
    if request.method == 'POST':
        print("Request post")
        form = JobDescriptionForm(request.POST)
        print(form, ' $$$$$$$$4 form')
        if form.is_valid():
            print('form valid')
            job = form.save(commit=False)
            description = request.POST['description']
            is_flagged = scan_job_description(description)
            status = 'Rejected' if is_flagged else 'Approved'
            job.description=description
            job.status=status
            job.save()
            return redirect('home')
        else:
            print("form not valid")
    else:
        form = JobDescriptionForm()
    return render(request, 'filter_app/post_job.html', {'form':form})

