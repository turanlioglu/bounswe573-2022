from django.shortcuts import render, redirect
from .forms import RegisterForm, UserProfileForm, ProfileUpdateForm
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
    if response.method == "POST":
        user_form = UserProfileForm(response.POST, instance = response.user)
        profile_form = ProfileUpdateForm(response.POST, response.FILES, instance = response.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(response, f'Your account has been updated, you can now login!')
            return redirect("/profile")
    else:
        user_form = UserProfileForm(instance = response.user)
        profile_form = ProfileUpdateForm(instance = response.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(response, "user/profile.html", context)