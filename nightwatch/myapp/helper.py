import random
from .models import *
import names

def get_new_dummy_User(is_male:bool = True):
    gender:str
    if is_male:
        gender = 'male'
    else:
        gender = 'female'
    first_name = names.get_first_name(gender=gender)
    last_name = names.get_last_name()
    username = first_name + "-" + last_name
    email = username + "+dummy@gmail.com"
    password = "12345678"
    new_user = User(username=username, email=email, password=password)
    new_user.save()
    return new_user

def get_new_dummy_NightwatchUser(user: User=None, moses:[MOS]=None):
    personal_numbers = [nw_user.personal_number for nw_user in NightwatchUser.objects.all()]
    personal_number = random.randint(99999, 9999999)
    while personal_number in personal_numbers:
        personal_number = random.randint(99999, 9999999)
    available = True
    nw_user = NightwatchUser(personal_number=personal_number, available=available)
    nw_user.save()
    rifleman = MOS.objects.get(name='Rifleman 07')
    if rifleman is not None:
        nw_user.mos.add(rifleman)
    if user is not None:
        nw_user.user = user
    if moses is not None:
        for mos in moses:
            nw_user.mos.add(mos)
    nw_user.save()
    return nw_user

def get_new_dummy_rifleman(moses:[MOS]=None):
    user = get_new_dummy_User()
    nw_user = get_new_dummy_NightwatchUser(user=user, moses=moses)
    return nw_user

def get_new_dummy_team(letter:chr=None, moses:[MOS]=None):
    marksman_mos = MOS.objects.get(name='Marksman')
    team_sargent_mos = MOS.objects.get(name="Team Sargent")
    grenadier_mos = MOS.objects.get(name="Grenadier")
    negev_mos = MOS.objects.get(name="Negev Operator")
    if moses is None:
        moses = [
            marksman_mos,
            team_sargent_mos,
            grenadier_mos,
            negev_mos
                 ]
    soldiers = [
        get_new_dummy_rifleman([mos]) for mos in moses
    ]
    soldiers.append(get_new_dummy_rifleman())
    for soldier in soldiers:
        print(soldier)
    if letter is None:
        letter = chr(random.randint(ord('A'),ord('Z')))
    team = Team(letter=letter)
    team.save()
    team_has_team_leader = False
    for soldier in soldiers:
        if team_sargent_mos in soldier.mos.all() and not team_has_team_leader:
            team.team_leader = soldier
            print(f"{soldier.user} is the team leader)")
            team_has_team_leader = True
        soldier.team = team
        soldier.save()
    team.save()
    return team


