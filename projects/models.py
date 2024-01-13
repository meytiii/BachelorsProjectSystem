from django.db import models
from users.models import karbar 
class Project(models.Model):
    title = models.CharField(max_length=255)
    professor = models.ForeignKey(karbar, on_delete=models.CASCADE)
    description = models.TextField(max_length=1024)
    is_available = models.BooleanField(default=True)
