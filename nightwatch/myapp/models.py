from django.db import models

class MOS(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Brigade(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    number = models.IntegerField(null=False)
    commander = models.ForeignKey('User', related_name='brigade_commander', on_delete=models.CASCADE, null=True, blank=True)
    second_commander = models.ForeignKey('User', related_name='brigade_second_commander', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.number}"


class Company(models.Model):
    letter = models.CharField(max_length=1, null=False)
    commander = models.ForeignKey('User', related_name='company_commander', on_delete=models.CASCADE, null=True, blank=True)
    second_commander = models.ForeignKey('User', related_name='company_second_commander', on_delete=models.CASCADE, null=True, blank=True)
    logistics_sargent = models.ForeignKey('User', related_name='company_logistics_sargent', on_delete=models.CASCADE, null=True, blank=True)
    brigade = models.ForeignKey(Brigade, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Company {self.letter}"


class Platoon(models.Model):
    letter = models.CharField(max_length=1, null=False)
    commander = models.ForeignKey('User', related_name='platoon_commander', on_delete=models.CASCADE, null=True, blank=True)
    sargent = models.ForeignKey('User', related_name='platoon_sargent', on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Platoon {self.letter}"


class Team(models.Model):
    letter = models.CharField(max_length=1, null=False)
    team_leader = models.ForeignKey('User', related_name='team_leader', on_delete=models.CASCADE, null=True, blank=True)
    platoon = models.ForeignKey(Platoon, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Team {self.letter}"


class User(models.Model):
    name = models.CharField(max_length=100, null=False)
    phone_number = models.CharField(max_length=15, null=False)
    email = models.EmailField(null=False)
    password = models.CharField(max_length=16, null=False, blank=False)
    personal_number = models.IntegerField(unique=True, null=False, blank=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    platoon = models.ForeignKey(Platoon, on_delete=models.CASCADE, null=True, blank=True)
    brigade = models.ForeignKey(Brigade, on_delete=models.CASCADE, null=True, blank=True)
    mos = models.ManyToManyField(MOS, through='UserMOS', blank=True)

    def __str__(self):
        return self.name + " " + str(self.personal_number)


class UserMOS(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.name} on Shift {self.shift.id}"
