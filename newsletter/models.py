from django.db import models

# Create your models here.
class Newsletter(models.Model):
    email = models.EmailField()
    full_name = models.CharField()
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)