from django.shortcuts import render
from django.https import HttpResponse

def index(request):
    #The Home page for learning-log
    return render(request, 'works/index.html')
