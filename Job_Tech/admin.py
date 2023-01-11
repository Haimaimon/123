from django.contrib import admin
from .models import  Job,StudentJobs,JobSeeker


admin.site.register(Job)
admin.site.register(StudentJobs)
admin.site.register(JobSeeker)