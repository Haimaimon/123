from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from tempfile import tempdir
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Job, StudentJobs
from .forms import  JobForm , CreateUserForm , StudentJobForm
from django.contrib.auth.forms import UserCreationForm

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

def view_jobs(request, id):
  jobs = Job.objects.get(pk=id)
  return HttpResponseRedirect(reverse('index'))

def my_profile(request):
    context = {}
    return render(request, 'profile.html',context)

def add(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            new_title = form.cleaned_data['title']
            new_desc = form.cleaned_data['desc']
            new_company = form.cleaned_data['company']

            Jobs = Job(
                title=new_title,
                desc=new_desc,
                company=new_company
            )
            Jobs.save()
            return render(request, 'add.html', {
                'form': JobForm(),
                'success': True
            })
    else:
        form = JobForm()
    return render(request, 'add.html', {
        'form': JobForm()
    })
def edit(request, id):
  if request.method == 'POST':
    jobs = Job.objects.get(pk=id)
    form = JobForm(request.POST, instance=jobs)
    if form.is_valid():
      form.save()
      return render(request, 'edit.html', {
        'form': form,
        'success': True
      })
  else:
    jobs = Job.objects.get(pk=id)
    form = JobForm(instance=jobs)
  return render(request, 'edit.html', {
    'form': form
  })

def delete(request, id):
  if request.method == 'POST':
    user = Job.objects.get(pk=id)
    user.delete()
  return HttpResponseRedirect(reverse('index'))

def studentjobs(request):
    studentjob = StudentJobs.objects.all()
    context ={
      'studentjob':studentjob,
    }
    return render(request, 'studentjob.html',context)
def index(request):
  jobs = Job.objects.all()
  context ={
        'jobs': jobs,
    }
  template = loader.get_template('index.html')
  return HttpResponse(template.render(context, request))