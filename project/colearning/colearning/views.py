from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList


def home(response):
    return render(response, "colearning/home.html", {})

def index(response, id):
    ls = ToDoList.objects.get(id = id)
    return render(response, "colearning/space.html", {"ls":ls})

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

