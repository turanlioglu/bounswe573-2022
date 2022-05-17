from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, searchBlog, LikeView
from . import views

urlpatterns = [
    path('', views.home, name = 'blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name = 'user-posts'),
    path('about/', views.about, name = 'blog-about'),
    path('feed/', PostListView.as_view(), name = "blog-feed"),
    path('post/<int:pk>', PostDetailView.as_view(), name = "post-detail"),
    path('q/', searchBlog, name = "search"),
    path('post/new/', PostCreateView.as_view(), name = "post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = "post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = "post-delete"),
    path('like/<int:pk>', LikeView, name = "like_post"),
    
    
] 