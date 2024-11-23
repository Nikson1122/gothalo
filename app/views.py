from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

# app/views.py
def report(request):
    return render(request, 'app/report.html')

def about(request):
    return render(request, 'app/about.html')

# def login_page(request):
#     return render(request, 'app/login.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            messages.success(request, "Account created successfully. Please log in.")
            return redirect('login')
    else:
        form =SignUpForm()
    return render(request, 'app/signup.html', {'form': form})





def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Welcome {user.username}!")
                return redirect('report')  # Replace 'home' with your desired URL name
    else:
        form = AuthenticationForm()
    return render(request, 'app/login.html', {'form': form})