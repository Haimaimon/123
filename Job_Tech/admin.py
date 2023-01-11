from django.contrib import admin
from .models import StudentJobs,JobSeeker,FileModel,Hr,AllJob



admin.site.register(StudentJobs)
admin.site.register(JobSeeker)
admin.site.register(Hr)
admin.site.register(AllJob)
admin.site.register(FileModel)