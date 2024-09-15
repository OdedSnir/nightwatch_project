import django.contrib.auth.models
from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone
from django.forms.models import model_to_dict
class MOS(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Brigade(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    number = models.IntegerField(null=False)
    commander = models.ForeignKey('NightwatchUser', related_name='brigade_commander', on_delete=models.CASCADE, null=True,
                                  blank=True)
    second_commander = models.ForeignKey('NightwatchUser', related_name='brigade_second_commander', on_delete=models.CASCADE,
                                         null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.number}"


class Company(models.Model):
    letter = models.CharField(max_length=1, null=False)
    commander = models.ForeignKey('NightwatchUser', related_name='company_commander', on_delete=models.CASCADE, null=True,
                                  blank=True)
    second_commander = models.ForeignKey('NightwatchUser', related_name='company_second_commander', on_delete=models.CASCADE,
                                         null=True, blank=True)
    logistics_sargent = models.ForeignKey('NightwatchUser', related_name='company_logistics_sargent', on_delete=models.CASCADE,
                                          null=True, blank=True)
    brigade = models.ForeignKey(Brigade, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):

        return f"Company {self.letter} of {str(self.brigade or '---') } brigade"


class Platoon(models.Model):
    letter = models.CharField(max_length=1, null=False)
    commander = models.ForeignKey('NightwatchUser', related_name='platoon_commander', on_delete=models.CASCADE, null=True,
                                  blank=True)
    sargent = models.ForeignKey('NightwatchUser', related_name='platoon_sargent', on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Platoon {self.letter}, {str(self.company or '---')}"


class Team(models.Model):
    letter = models.CharField(max_length=1, null=False)
    team_leader = models.ForeignKey('NightwatchUser', related_name='team_leader', on_delete=models.CASCADE, null=True, blank=True)
    platoon = models.ForeignKey(Platoon, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Team {self.letter}, {str(self.platoon or '---')}"


class NightwatchUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    personal_number = models.IntegerField(unique=True, null=False, blank=False)
    available = models.BooleanField(default=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    platoon = models.ForeignKey(Platoon, on_delete=models.CASCADE, null=True, blank=True)
    brigade = models.ForeignKey(Brigade, on_delete=models.CASCADE, null=True, blank=True)
    mos = models.ManyToManyField(MOS, through='UserMOS', blank=True)


    def __str__(self):
        if self.user is not None:
            return self.user.username + " " + str(self.personal_number)
        else:
            return "Nightwatch User" + " " + str(self.personal_number)

    def get_presentable_dict(self):
        dict = model_to_dict(self)
        if self.brigade is not None:
            dict['brigade'] = self.brigade.name
        if self.company is not None:
            dict['company'] = self.company.letter
        if self.platoon is not None:
            dict['platoon'] = self.platoon.letter
        if self.team is not None:
            dict['team'] = self.team.letter
        return dict


    def delete_with_user(self):
        if self.user is not None:
            user:User = self.user
            user.delete()
        self.delete()

class UserMOS(models.Model):
    user = models.ForeignKey(NightwatchUser, on_delete=models.CASCADE)
    mos = models.ForeignKey(MOS, on_delete=models.CASCADE)
    date_assigned = models.DateField(null=True, blank=True)  # Optional: to track when the MOS was assigned

    def __str__(self):
        return f"{self.user.name} - {self.mos.name}"


class Mission(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    demanded_mos = models.ForeignKey(MOS, on_delete=models.CASCADE)
    shift_hour_length = models.IntegerField()
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Shift(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return f"Shift {self.id} - {self.position.name}"


class UserShift(models.Model):
    user = models.ForeignKey(NightwatchUser, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.name} on Shift {self.shift.id}"


def delete_users_and_NWUsers_by_hour_back(hours:int = 1):
    if hours >= 1:
        now = timezone.now()
        hours_back = now - timedelta(hours=hours)
        users_ids =[
            item['id'] for item in User.objects.filter(date_joined__gte=hours_back).values('id')
        ]
        nw_users = NightwatchUser.objects.filter(user__id__in=users_ids)
        for nw_user in nw_users:
            nw_user.delete_with_user()

def delete_team_with_users(team:Team):
    nw_users = NightwatchUser.objects.filter(team=team)
    for nw_user in nw_users:
        nw_user.delete_with_user()
    team.delete()