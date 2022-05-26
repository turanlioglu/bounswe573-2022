from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post, Comment, Category
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.PostListView = reverse('blog-feed')
   


    def test_PostListView_GET(self):
        response = self.client.get(self.PostListView)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/feed.html')
