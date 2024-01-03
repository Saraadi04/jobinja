from django.http import HttpResponse, JsonResponse
from works.models import Job,JobSeeker,Company,Provinces,Category
from django.shortcuts import render
from django.contrib import messages
from persiantools.jdatetime import JalaliDate
import holidays
import requests


def landing(request):
    jobs = Job.objects.all() 
    f_list= {
        "jobs": jobs
        } 
    return render(request, 'works/landing.html', context=f_list)


def detail(request,id):
    if request.method == 'GET':
        try:
            jobs = Job.objects.get(pk=id)
        except:
            jobs = None
        j_list = {
            'jobs' : jobs, 
            'flag' : False
        }
        return render(request, 'works/detail.html', context=j_list)
    

def provinceview(request):
    provinces = Provinces.objects.all() 
    return provinces


def my_view(request):
  # Get the current date in the Jalali calendar
  current_date = JalaliDate.today()

  # Format the date as YYYY/MM/DD
  date_str = f"{current_date.year}/{current_date.month}/{current_date.day}"

  # Send a GET request to the API
  response = requests.get(f'https://holidayapi.ir/jalali/{date_str}')

  # Parse the JSON response
  data = response.json()

  # Check if today is a holiday
  if data['is_holiday']:
      message = "Due to recent holiday, your request may exprience delay.we appreciate your understanding."
  else:
      message = None

  # Render the template
  return render(request, 'works/message.html', context = message)


    