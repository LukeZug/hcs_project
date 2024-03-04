from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .models import PasswordChoice, PasswordGuess, ShoulferSurferGuess
import random

# Create your views here.
def part_1(request):
    context = {}
    return render(request, 'emoji_password_evaluation/part_1.html', context=context)

def part_2(request):
    context = {}
    return render(request, 'emoji_password_evaluation/part_2.html', context=context)

def part_3(request):
    context = {}
    return render(request, 'emoji_password_evaluation/part_3.html', context=context)

def submit_passwords(request):
    if request.method == 'POST':
        # Generate a random number
        identifier = random.randint(100000, 999999)

        # Process each password
        for key in request.POST:
            if key.startswith('password'):
                password = request.POST[key]
                PasswordChoice.objects.create(password=password, identifier=str(identifier))

        # Set the identifier in the user's cookie
        response = redirect('emoji_password_evaluation:part_2')
        response.set_cookie('identifier', identifier)

        return response

    return redirect('part_1')

def submit_recall_passwords(request):
    if request.method == 'POST':
        identifier = request.COOKIES.get('identifier')

        if not identifier:
            return HttpResponse("Identifier not found.")

        # Check each guess
        for i in range(1, 7):
            guess_key = f'guess{i}'
            guess = request.POST.get(guess_key, '')

            # Save the guess
            PasswordGuess.objects.create(identifier=identifier, password_guess=guess)

        return redirect('emoji_password_evaluation:finished')

    return redirect('emoji_password_evaluation:part_3')

def submit_surfer_guesses(request):
    if request.method == 'POST':
        identifier = request.COOKIES.get('identifier')

        # Process each password
        question_number = 1
        for key in request.POST:
            if key.startswith('password'):
                password = request.POST[key]
                ShoulferSurferGuess.objects.create(identifier=str(identifier), password_guess=password, question_number=question_number)
                question_number += 1

        # Set the identifier in the user's cookie
        response = redirect('emoji_password_evaluation:part_3')
        return response

    return redirect('emoji_password_evaluation:part_2')

def finished(request):
    return render(request, 'emoji_password_evaluation/finished.html', context={})
