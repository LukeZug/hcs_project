from django.db import models

# Create your models here.
class PasswordChoice(models.Model):
    password = models.TextField()
    identifier = models.TextField()

    def __str__(self):
        return f'{self.identifier} -> {self.password}'

class PasswordGuess(models.Model):
    identifier = models.TextField()
    password_guess = models.TextField()

    def __str__(self):
        return f'{self.identifier} -> {self.password_guess}'
    
class ShoulferSurferGuess(models.Model):
    identifier = models.TextField()
    password_guess = models.TextField()
    question_number = models.IntegerField()

    def __str__(self):
        return f'{self.identifier} -> {self.password_guess} (Q{self.question_number})'
    