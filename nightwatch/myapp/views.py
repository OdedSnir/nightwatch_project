from django.http import HttpResponse, HttpRequest, JsonResponse
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserForm, NightwatchUserForm



# Create your views here.
# handles the request responce logic for your app

def index(request: HttpRequest) -> HttpResponse: # not used anymore
    MOSs = MOS.objects.all()
    context = {"MOSs": MOSs}
    return render(request, 'index.html', context=context)

def load_companies(request: HttpRequest):
    brigade_id = request.GET.get('brigade_id')
    if brigade_id:
        companies = Company.objects.filter(brigade_id=brigade_id).order_by('letter')
    else:
        companies = Company.objects.all().order_by('letter')
    return JsonResponse(list(companies.values('id', 'letter')), safe=False)


def load_platoons(request: HttpRequest):
    company_id = request.GET.get('company_id')
    if company_id:
        platoons = Platoon.objects.filter(company_id=company_id).order_by('letter')
    else:
        platoons = Platoon.objects.all().order_by('letter')
    return JsonResponse(list(platoons.values('id', 'letter')), safe=False)



def load_teams(request: HttpRequest):
    platoon_id = request.GET.get('platoon_id,')
    if platoon_id:
        teams = Team.objects.filter(platoon_id=platoon_id,).order_by('letter')
    else:
        teams = Team.objects.all().order_by('letter')
    return JsonResponse(list(teams.values('id', 'letter')), safe=False)


def register(request: HttpRequest):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        nightwatch_form = NightwatchUserForm(request.POST)

        if user_form.is_valid() and nightwatch_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            nightwatch_user = nightwatch_form.save(commit=False)
            nightwatch_user.user = user
            nightwatch_user.save()

            login(request, user)
            return redirect('index')
    else:
        user_form = UserForm()
        nightwatch_form = NightwatchUserForm()

    return render(request, 'register.html', {'user_form': user_form, 'nightwatch_form': nightwatch_form})

def profile_view(request: HttpRequest):
    user = request.user
    profile_data:dict = {}
    if user is not None and user.is_authenticated:
        profile_data.update(model_to_dict(user))
        nightwatch_user = NightwatchUser.objects.filter(user=user).first()
        if nightwatch_user is not None:
            profile_data.update(nightwatch_user.get_presentable_dict())

    return render(request, 'index.html', {'profile_data': profile_data})


