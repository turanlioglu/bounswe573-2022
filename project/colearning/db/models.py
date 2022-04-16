from django.db import models

# Create your models here.
class Space(models.Model):
    title = models.TextField()
    content = models.TextField()