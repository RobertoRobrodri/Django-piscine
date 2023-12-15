from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def history(request):
    template = loader.get_template('history.html')
    return HttpResponse(template.render())