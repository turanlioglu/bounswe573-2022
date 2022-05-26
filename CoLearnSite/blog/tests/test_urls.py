from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, searchBlog, LikeView

class TestUrls(SimpleTestCase):

    def test_list_url_resolves(self):
        url = reverse('blog-feed')
        self.assertEquals(resolve(url).func.view_class, PostListView)

    def test_user_list_url_resolves(self):
        url = reverse('user-posts', args = ['username'])
        self.assertEquals(resolve(url).func.view_class, UserPostListView)

    def test_create_url_resolves(self):
        url = reverse('post-create')
        self.assertEquals(resolve(url).func.view_class, PostCreateView)

    def test_update_url_resolves(self):
        url = reverse('post-update', kwargs = {'pk' : 1})
        self.assertEquals(resolve(url).func.view_class, PostUpdateView)

    def test_delete_url_resolves(self):
        url = reverse('post-delete', kwargs = {'pk' : 1})
        self.assertEquals(resolve(url).func.view_class, PostDeleteView)
    
    def test_detail_url_resolves(self):
        url = reverse('post-detail', kwargs = {'pk' : 1})
        self.assertEquals(resolve(url).func.view_class, PostDetailView)

    def test_like_url_resolves(self):
        url = reverse('like_post', kwargs = {'pk' : 1})
        self.assertEquals(resolve(url).func, LikeView)