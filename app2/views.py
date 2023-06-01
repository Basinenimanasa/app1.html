from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def app2_string(request):
    return HttpResponse('<h1>This is third project</h1>')
