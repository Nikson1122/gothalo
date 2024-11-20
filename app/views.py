from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

# app/views.py
def report(request):
    return render(request, 'app/report.html')

def about(request):
    return render(request, 'app/about.html')