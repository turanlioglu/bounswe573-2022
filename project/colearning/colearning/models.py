from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length = 100, null = True)
    content = models.TextField(null = True)
    date_posted = models.DateTimeField(default = timezone.now, null = True)
    author = models. ForeignKey(User, on_delete = models. CASCADE, null = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs = {'pk': self.pk})