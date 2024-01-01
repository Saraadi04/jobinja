from django.urls import path
from .views import  home, landing, detail


urlpatterns = [
    path('', home, name='home'),
    path('home', home, name='home'),
    path('jobs', landing, name="job's list"),
    path('<str:code>', detail, name="job's details"),
    
]