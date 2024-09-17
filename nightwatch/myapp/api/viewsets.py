from rest_framework import viewsets
from ..models import Company, Platoon, Team
from .serializer import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = MyUserSerializer

class NightwatchUserViewSet(viewsets.ModelViewSet):
    queryset = NightwatchUser.objects.all()
    serializer_class = NightwatchUserSerializer


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



