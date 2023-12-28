from django.db import models

class JobListing(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title
