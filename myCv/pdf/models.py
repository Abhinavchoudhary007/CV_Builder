from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    summary = models.TextField()
    degree = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    previous_experience = models.TextField()
    skills = models.TextField()

    def __str__(self):
        return self.name