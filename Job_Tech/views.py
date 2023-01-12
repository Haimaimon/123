from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from tempfile import tempdir
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import StudentJobs,JobSeeker,Hr,AllJob,FileModel
from .forms import CreateUserForm , StudentJobForm,JobSeekerForm,HrForm,AllJobsForm,FileUploadForm
from django.contrib.auth.forms import UserCreationForm
from .filters import AllJobFilter

# Create your views here.

def home(request):
  jobs = Job.objects.all()
  context = {
    'jobs': jobs
  }
  return render(request, 'home.html',context)

def registerPage(request):
      form = CreateUserForm()
      if request.method == 'POST':

          form = CreateUserForm(request.POST)
          if form.is_valid():
              form.save()
              user = form.cleaned_data.get('username')
              messages.success(request, 'Account was created for ' + user)
              return redirect('index')

      context = {'form': form}
      return render(request, 'register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'username OR password is incorrect')
    context = {}
    return render(request, 'login.html', context)
def logoutUser(request):
  logout(request)
  return redirect('login')
def view_jobs(request, id):
  allJobs = AllJob.objects.get(pk=id)
  return HttpResponseRedirect(reverse('index'))


def my_profile(request):
    hr = request.user.hr
    form = HrForm(instance=hr)

    if request.method == 'POST':
        form = HrForm(request.POST, instance=hr)
        if form.is_valid():
            print('succsed')
            form.save()

    context = {
        'form': form
    }
    return render(request, 'profile.html', context)

def add(request):
    if request.method == 'POST':
        form = AllJobsForm(request.POST)
        if form.is_valid():
            new_hr = form.cleaned_data['hr']
            new_title = form.cleaned_data['title']
            new_desc = form.cleaned_data['desc']
            new_company = form.cleaned_data['company']
            new_location = form.cleaned_data['location']

            Alljobs = AllJob(
                hr=new_hr,
                title=new_title,
                desc=new_desc,
                company=new_company,
                location=new_location
            )
            Alljobs.save()
            return render(request, 'add.html', {
                'form': AllJobsForm(),
                'success': True
            })
    else:
        form = AllJobsForm()
    return render(request, 'add.html', {
        'form': AllJobsForm()
    })
def edit(request,id):
  alljobs = AllJob.objects.get(pk=id)
  form = AllJobsForm(request.POST, instance=alljobs)
  if request.method == 'POST':
    if form.is_valid():
      form.save()
      return render(request, 'edit.html', {
        'form': form,
        'success': True
      })
  else:
    alljobs = AllJob.objects.get(pk=id)
    form = AllJobsForm(instance=alljobs)
  return render(request, 'edit.html', {
    'form': form
  })

def delete(request, id):
  if request.method == 'POST':
    alljobs = AllJob.objects.get(pk=id)
    alljobs.delete()
  return HttpResponseRedirect(reverse('user'))

def studentjobs(request):
    studentjob = StudentJobs.objects.all()
    context ={
      'studentjob':studentjob,
    }
    return render(request, 'studentjob.html',context)

def userPage(request):
    allJobs = AllJob.objects.all()
    myFilter = AllJobFilter(request.GET, queryset=allJobs)
    allJobs = myFilter.qs

    context = {
        'alljobs': allJobs,
        'myFilter': myFilter,
    }

    return render(request, 'jobseeker.html', context)

def userr(request):
  alljobs = request.user.hr.alljob_set.all()
  print('ALLJOBS',alljobs)
  context = {
    'alljobs': alljobs,
  }
  return render(request, 'user.html', context)


def profileseeker(request):
    jobseeker = request.user.jobseeker
    form = JobSeekerForm(instance=jobseeker)

    if request.method == 'POST':
        form = JobSeekerForm(request.POST, instance=jobseeker)
        if form.is_valid():
            jobseeker.save()
            user = request.user
            user.save()
            print('succsed')
            form.save()

    context = {
        'form': form
    }
    return render(request, 'profileseeker.html', context)

def portFolio(request):
  files = request.user.jobseeker.filemodel_set.all()
  context = {
    'files': files,
  }
  return render(request, 'portfolio.html',context)

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio')
    else:
        form = FileUploadForm()
    return render(request, 'upload.html', {'form': form})
def deleteProfile(request):
    hr = request.user.hr
    form = HrForm(instance=hr)
    if request.method == 'POST':
        hr.delete()
        user = request.user
        user.delete()
        return redirect('home')
    context = {
      'form':form
    }
    return render(request,'delete.html',context)

def search_job(request):
  allseeker = JobSeeker.objects.all()
  files = FileModel.objects.all()
  context = {
    'allseeker':allseeker,
    'files':files
  }
  return render(request,'searchjob.html',context)

def submission(request):
  context = {}
  return render(request, 'job_submission.html',context)