from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    interested_categories = models.TextField()

class SpaceCategory(models.Model):
    space_name = models.CharField(max_length = 100, null = True)
    description = models.TextField(null = True)

    class Meta:
        verbose_name_plural = "Space Categories"

class Space(models.Model):
    category = models.ForeignKey(SpaceCategory, on_delete = models.CASCADE, null = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    space_name = models.CharField(max_length = 100, null = True)
    description = models.TextField(null = True)