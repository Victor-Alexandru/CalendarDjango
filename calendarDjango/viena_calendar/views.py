from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Day


def index(request):
    days = Day.objects.all()
    context = {
        'days': days
    }
    return render(request, 'viena_calendar/index.html', context)
# Create your views here.
