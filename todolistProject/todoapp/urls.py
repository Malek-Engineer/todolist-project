from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='todoapp-home'),
    path('about/', views.about, name='todoapp-about'),
    path('connexion', views.connexion, name='todoapp-connexion')
]