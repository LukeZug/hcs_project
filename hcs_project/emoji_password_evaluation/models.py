from django.db import models

# Create your models here.
class PasswordChoice(models.Model):
    password = models.TextField()
    identifier = models.TextField()

class PasswordGuess(models.Model):
    identifier = models.TextField()
    password_guess = models.TextField()
    