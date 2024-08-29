from django.contrib import admin
from .models import *
# Register your models here.
# allows a user friendly interface to interact with the models directly from the interface
# Register your models here.
admin.site.register(User)
admin.site.register(Brigade)
admin.site.register(Company)
admin.site.register(Platoon)
admin.site.register(Team)
admin.site.register(Mission)
admin.site.register(Position)
admin.site.register(Shift)
admin.site.register(UserShift)
admin.site.register(MOS)
admin.site.register(UserMOS)
