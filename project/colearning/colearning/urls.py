"""colearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from user import views as v


urlpatterns = [
    path('admin/', admin.site.urls),
    path("space/", views.index, name = "index"),
    path("", PostListView.as_view(), name = "home"),
    path("about/", views.about, name = "about"),
    path("register/", v.register, name = "register"),
    path("profile/", v.profile, name = "profile"),
    path("login/", auth_views.LoginView.as_view(template_name = "user/login.html"), name = "login"),
    path("logout/", auth_views.LogoutView.as_view(template_name = "user/logout.html"), name = "logout"),
    path("post/<int:pk>/", PostDetailView.as_view(), name = "post_detail"),
    path("post/new/", PostCreateView.as_view(), name = "post_create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name = "post_update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name = "post_delete"),
    path("user<str:username>/", UserPostListView.as_view(), name = "user_posts"),
    path("", include("django.contrib.auth.urls")),
    path("help/", views.help, name = "help")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
