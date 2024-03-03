from django.contrib import admin
from .models import PasswordChoice, PasswordGuess

# Register your models here.
admin.site.register(PasswordChoice)
admin.site.register(PasswordGuess)
