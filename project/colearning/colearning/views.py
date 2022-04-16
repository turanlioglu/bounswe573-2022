from django.shortcuts import render
from django.http import HttpResponse
from .forms import CreateNewList


def home(response):
    return render(response, "colearning/home.html", {})


def create(response):
    form = CreateNewList()
    return render(response, "colearning/create.html", {"form":form})