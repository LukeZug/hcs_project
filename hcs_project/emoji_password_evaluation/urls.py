from django.contrib import admin
from django.urls import path, include
from emoji_password_evaluation import views

app_name = 'emoji_password_evaluation'

urlpatterns = [
    path('submit_passwords/', views.submit_passwords, name='submit_passwords'),
    path('recall_passwords/', views.part_3, name='part_3'),
    path('shoulder_surfer/', views.part_2, name='part_2'),
    path('submit_recall_passwords/', views.submit_recall_passwords, name='submit_recall_passwords'),
    path('submit_surfer_guesses/', views.submit_surfer_guesses, name='submit_surfer_guesses'),
    path('finished/', views.finished, name='finished'),
]