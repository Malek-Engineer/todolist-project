from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'todoapp/home.html')


def about(request):
    return render(request, 'todoapp/about.html')


def connexion(request): 
    return render(request, 'todoapp/connexion.html')