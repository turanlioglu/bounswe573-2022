from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import DetailView, CreateView
from .models import Post, Item
from .forms import CreateNewList


def home(response):
    context = {
        'posts': Post.objects.all()
    }
    return render(response, "colearning/home.html", context)

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['space_name', 'title', 'content']


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