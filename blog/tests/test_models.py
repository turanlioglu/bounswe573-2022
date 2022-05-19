from django.test import TestCase
from blog.models import Post, Comment, Category
from django.urls import reverse

class TestModels(TestCase):

    def test_model_str(TestCase):
        title = Post.objects.create(title = "Post 1")
        content = Post.objects.create(content = "This is some content")
        self.assertEquals(str(title), "Post 1")