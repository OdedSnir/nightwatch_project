from rest_framework import viewsets, filters
from ..models import Company, Platoon, Team
from .serializer import *
from django_filters.rest_framework import DjangoFilterBackend

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = MyUserSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_fields = ['username', 'email', 'first_name', 'last_name']
    search_fields = ['username', 'email', 'first_name', 'last_name']

class NightwatchUserViewSet(viewsets.ModelViewSet):
    queryset = NightwatchUser.objects.all()
    serializer_class = NightwatchUserSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_fields = ['personal_number', 'available', 'brigade', 'company', 'platoon',  'team', 'mos']
    search_fields = ['personal_number', 'available', 'brigade', 'company', 'platoon', 'team', 'mos']

class BrigadeViewSet(viewsets.ModelViewSet):
    queryset = Brigade.objects.all()
    serializer_class = BrigadeSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class PlatoonViewSet(viewsets.ModelViewSet):
    queryset = Platoon.objects.all()
    serializer_class = PlatoonSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class MOSViewSet(viewsets.ModelViewSet):
    queryset = MOS.objects.all()
    serializer_class = MosSerializer



