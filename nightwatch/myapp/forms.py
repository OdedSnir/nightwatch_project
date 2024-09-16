from django import forms
from django.contrib.auth.models import User
from .models import *
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']


class NightwatchUserForm(forms.ModelForm):
    mos = forms.ModelMultipleChoiceField(
        queryset=MOS.objects.order_by('name'),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    class Meta:
        model = NightwatchUser
        fields = ['personal_number', 'available', 'brigade', 'company', 'platoon',  'team', 'mos']

    def __init__(self, *args, **kwargs):
        super(NightwatchUserForm, self).__init__(*args, **kwargs)
        self.fields['company'].queryset = Company.objects.none()
        self.fields['platoon'].queryset = Platoon.objects.none()
        self.fields['team'].queryset = Team.objects.none()
        self.fields['mos'].queryset = MOS.objects.order_by('name')
        if 'brigade' in self.data:
            try:
                brigade_id = int(self.data.get('brigade'))
                self.fields['company'].queryset = Company.objects.filter(brigade_id=brigade_id).order_by('letter')
            except (ValueError, TypeError) as error:
                print(error)
        elif self.instance.pk and self.instance.brigade:
            self.fields['company'].queryset = Company.objects.filter(brigade=self.instance.brigade).order_by('letter')

        if 'company' in self.data:
            try:
                company_id = int(self.data.get('company'))
                self.fields['platoon'].queryset = Platoon.objects.filter(company_id=company_id).order_by('letter')
            except (ValueError, TypeError) as error:
                print(error)
        elif self.instance.pk and self.instance.company:
            self.fields['platoon'].queryset = Platoon.objects.filter(company=self.instance.company).order_by('letter')

        if 'platoon' in self.data:
            try:
                platoon_id = int(self.data.get('platoon'))
                self.fields['team'].queryset = Team.objects.filter(platoon_id=company_id).order_by('letter')
            except (ValueError, TypeError) as error:
                print(error)
        elif self.instance.pk and self.instance.platoon:
            self.fields['team'].queryset = Team.objects.filter(platoon=self.instance.platoon).order_by('letter')

