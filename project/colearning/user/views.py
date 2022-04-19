from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(response, f'Your account has been created, you can now login!')
            return redirect("login")
    else:   
        form = RegisterForm()
    return render(response, "user/register.html", {"form":form})

@login_required()
def profile(response):
    return render(response, "user/profile.html", {})