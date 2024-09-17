from django.urls import path, include
from . import views
from .api import api
from django.contrib.auth import views as auth_views
from rest_framework import routers
from .api.viewsets import *
#define a list of url patterns
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'nightwatch_users', NightwatchUserViewSet)
router.register(r'brigades', BrigadeViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'platoons', PlatoonViewSet)
router.register(r'teams', TeamViewSet)

urlpatterns = [
    path('', views.profile_view, name= "home"),
    path('api/sample', api.sample, name='sample'),
    path('api/', include(router.urls)),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('ajax/load-companies/', views.load_companies, name='ajax_load_companies'),
    path('ajax/load-platoons/', views.load_platoons, name='ajax_load_platoons'),
    path('ajax/load-teams/', views.load_teams, name='ajax_load_teams'),
]
