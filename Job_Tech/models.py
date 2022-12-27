from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    company = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title}, {self.desc}, {self.company}'
