from django.contrib import admin
from .models import PasswordChoice, PasswordGuess, ShoulferSurferGuess

# Register your models here.
admin.site.register(PasswordChoice)
admin.site.register(PasswordGuess)
admin.site.register(ShoulferSurferGuess)
