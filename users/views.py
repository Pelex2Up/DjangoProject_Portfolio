from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.urls import reverse
from users.forms import CustomUserCreationForm, CustomLoginForm


def dashboard(request):
    return render(request, "users/dashboard.html")


def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            user.save()
            login(request, user)
            return redirect(reverse("dashboard"))


def modal_login(request):
    context = {}
    login_modal = get_object_or_404(CustomLoginForm)
    context['login_modal'] = login_modal
    return render(request, 'registration/login.html', context)