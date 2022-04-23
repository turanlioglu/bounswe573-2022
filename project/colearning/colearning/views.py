from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import CreateNewList



posts = [
    {
        'author': 'erdemturanlioglu',
        'title': 'new post 1',
        'content': 'first post',
        'date_posted': 'April 23, 2022'
    }
]

def home(response):
    context = {
        'posts': Post.objects.all()
    }
    return render(response, "colearning/home.html", context)

class PostListView(ListView):
    model = Post
    template_name = "colearning/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 7

class UserPostListView(ListView):
    model = Post
    template_name = "colearning/user_post.html"
    context_object_name = "posts"
    paginate_by = 7

    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

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
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(response):
    return render(response, "colearning/about.html", {})

def index(response):
    return render(response, "colearning/space.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name = n)
            t.save()
        
        return HttpResponseRedirect("/%i" %t.id)

    else: 
        form = CreateNewList()
    return render(response, "colearning/create.html", {"form":form})

def help(response):
    return render(response, "colearning/help.html", {})