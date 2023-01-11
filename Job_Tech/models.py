from django.db import models


class Hr(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    placejob = models.CharField(max_length=50, null=True)
    usertype = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.user}'
class AllJob(models.Model):
    AGE = (
         ('18-24','18-24'),
         ('25-35','25-35'),
         ('35+','35+'),
    )
    hr = models.ForeignKey(Hr, null=True, on_delete= models.SET_NULL)
    title = models.CharField(max_length=80)
    desc = models.TextField()
    company = models.CharField(max_length=40)
    location = models.CharField(max_length=30)
    age = models.CharField(max_length=10, null=True,choices=AGE)
class StudentJobs(models.Model):
    title = models.CharField(max_length=80)
    desc = models.TextField()
    company = models.CharField(max_length=40)
    location = models.CharField(max_length=30)

    def _str_(self):
        return f'{self.title}, {self.desc}, {self.company},{self.location}'

class JobSeeker(models.Model):
    EDUCATION = (
         ('Software Engineering', 'Software Engineering'),
         ('Computer Science', 'Computer Science'),
         ('Information Systems', 'Information Systems'),
         ('Full-Stack Course', 'Full-Stack Course'),
         ('12 school years', '12 school years'),
    )
    WORKWITHINITIATOR = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    education = models.CharField(max_length=50, null=True, choices=EDUCATION)
    wordwithinitiator = models.CharField(max_length=50, null=True, choices=WORKWITHINITIATOR)

    def _str_(self):
        return f'{self.user}'