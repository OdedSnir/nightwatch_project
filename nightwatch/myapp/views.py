from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import MOS


# Create your views here.
# handles the request responce logic for your app

def index(request: HttpRequest) -> HttpResponse:
    MOSs = MOS.objects.all()
    context = {"MOSs": MOSs}
    return render(request, 'index.html', context=context)
