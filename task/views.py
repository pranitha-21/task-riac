from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def committees(request):
    return render(request, 'committee.html')

def events(request):
    return render(request, 'events.html')
