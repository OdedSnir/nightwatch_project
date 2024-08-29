from django.urls import path
from . import views
from .api import api
#define a list of url patterns
urlpatterns = [
    path('', views.index, name= "index"),
    path('api/sample', api.sample, name='sample'),
]
