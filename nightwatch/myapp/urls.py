from django.urls import path
from . import views
from .api import api
#define a list of url patterns
urlpatterns = [
    path('', views.index, name= "index"),
    path('api/sample', api.sample, name='sample'),
    path('register/', views.register, name='register'),
    path('ajax/load-companies/', views.load_companies, name='ajax_load_companies'),
    path('ajax/load-platoons/', views.load_platoons, name='ajax_load_platoons'),
    path('ajax/load-teams/', views.load_teams, name='ajax_load_teams'),
]
