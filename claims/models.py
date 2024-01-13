from django.db import models
from users.models import karbar
from projects.models import Project

class Claim(models.Model):
    student = models.ForeignKey(karbar, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    classmates = models.ManyToManyField(karbar, related_name='classmates', blank=True)
    claim_status = models.CharField(max_length=10, default='pending')
