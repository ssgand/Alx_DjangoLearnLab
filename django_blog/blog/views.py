from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages

from .forms import RegisterForm, ProfileUpdateForm


# --- LOGIN VIEW ---
# class UserLoginView(LoginView):
    # template_name = 'blog/login.html'

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'blog/login.html')


# --- LOGOUT VIEW ---
# class UserLogoutView(LogoutView):
#     template_name = 'blog/logout.html'

def logout_user(request):
    logout(request)
    return redirect('login')


# --- REGISTRATION / SIGNUP ---
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})


# --- PROFILE VIEW (VIEW + EDIT PROFILE) ---
@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, 'blog/profile.html', {'form': form})

def home(request):
    return render(request, "blog/home.html")

def posts(request):
    return render(request, "blog/posts.html")

