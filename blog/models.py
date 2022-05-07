from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from hitcount.models import HitCount
from django.contrib.contenttypes.fields import GenericRelation
from taggit.managers import TaggableManager

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length = 20)

    def __str__(self):
        return self.title
        class Meta:
            verbose_name = "Category"
            verbose_name_plural = "Categories"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    date_posted = models.DateField(auto_now_add = True)
    post = models.ForeignKey('Post', on_delete = models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.username

class Space(models.Model):
    space = models.CharField(max_length = 25)

class Post(models.Model):
    spaces = models.ManyToManyField(Space)
    title = models.CharField(max_length = 100)
    content = RichTextField()
    image = models.ImageField(null = True, blank = True, upload_to = 'media')
    image_url = models.CharField(max_length = 100, default = None, null = True, blank = True)
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    tags = TaggableManager()
    hit_count_generic = GenericRelation(HitCount, object_id_field = "object_pk", related_query_name = "hit_count_generic_relation")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs = {'pk': self.pk})
