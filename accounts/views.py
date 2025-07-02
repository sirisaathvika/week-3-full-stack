from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib import messages

# Register
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('verify', token='dummy-token')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Simulated Verification
def verify(request, token):
    messages.success(request, "Account Verified Successfully ✅")
    return render(request, 'verify.html')

# Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'login.html')

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')

# Protected Dashboard
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
