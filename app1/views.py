from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def app1_string(request):
    return HttpResponse('<h1>This is second project</h1>')
