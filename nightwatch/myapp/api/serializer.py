from rest_framework.serializers import ModelSerializer
from ..models import *


class MyUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email',]
        read_only_fields = ['id',]


class NightwatchUserSerializer(ModelSerializer):
    class Meta:
        model = NightwatchUser
        fields = ['id', 'personal_number', 'available', 'brigade', 'company', 'platoon',  'team', 'mos']
        read_only_fields = ['id']
        depth = 1


class BrigadeSerializer(ModelSerializer):
    class Meta:
        model = Brigade
        fields = ['id', 'name', 'number']
        read_only_fields = ['id']


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'letter']


class PlatoonSerializer(ModelSerializer):
    class Meta:
        model = Platoon
        fields = ['id', 'letter']


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'letter']


class MosSerializer(ModelSerializer):
    class Meta:
        model = MOS
        fields = ['id', 'name', 'description']
