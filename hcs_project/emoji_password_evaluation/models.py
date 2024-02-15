from django.db import models

# Create your models here.
class Word(models.Model):
    text = models.TextField()
    
class UserResponse(models.Model):
    word_text = models.TextField()
    user_input = models.TextField()
    duration = models.IntegerField(null=True)
    