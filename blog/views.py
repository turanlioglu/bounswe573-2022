from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, Category
from courses.models import Course
from hitcount.views import HitCountDetailView
from blog.forms import CommentForm
from django.db.models import Q


# Create your views here.
@login_required
def searchBlog(request):
    context = {}
    posts = Post.objects.all()
    if request.method == "GET":
        query = request.GET.get("search")
        queryset = posts.filter(Q(title_icontains = query))
        total = queryset.count()
        context.update({
            'total': total,
            'query': query,
            'posts': queryset
        })
        return render(request, "blog/search_blog.html", context)


def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

@login_required
def feed(request):
    context = []
    posts = Post.objects.all()
    categories = Category.objects.all()
    popular_posts = Post.objects.order_by('hit_count_generic')[:3]
    context = {
        'popular_posts': popular_posts,
        'categories': categories,
        'posts': posts,
    }
    return render(request, 'blog/feed.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/feed.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')

class PostDetailView(HitCountDetailView):
    model = Post
    count_hit = True
    form = CommentForm()

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()

            return redirect(reverse("post-detail", kwargs = {
                'pk': post.pk
            }))
    
    def get_context_data(self, **kwargs):
        similar_posts = self.object.tags.similar_objects()[:3]
        post_comments_count = Comment.objects.all().filter(post = self.object.id).count()
        post_comments = Comment.objects.all().filter(post = self.object.id)
        context = super().get_context_data(**kwargs)
        context.update({
            'form': self.form,
            'post_comments': post_comments,
            'post_comments_count': post_comments_count,
            'similar_posts': similar_posts,
        })
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['course', 'title', 'content', 'image', 'image_url', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['course', 'title', 'content', 'image', 'image_url', 'tags']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "{{ url 'post-detail'}}"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False