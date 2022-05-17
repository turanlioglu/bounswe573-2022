from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post, Comment, Category
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.PostListView = reverse('blog-feed')
        self.PostDetailView = reverse('post-detail', kwargs = {'pk' : 1})

    def test_PostListView_GET(self):
        client = Client()
        response = self.client.get(self.PostListView)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/feed.html')

    def test_PostDetailView_GET(self):
        client = Client()
        response = self.client.get(self.PostDetailView)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')