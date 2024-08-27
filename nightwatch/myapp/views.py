from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# handles the request responce logic for your app

def index(request):
    return HttpResponse("MyApp")