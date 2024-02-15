from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Word, UserResponse
import random
import json

# Create your views here.
def index(request):
    context = {}
    return render(request, 'emoji_password_evaluation/index.html', context=context)

@require_http_methods(["GET"])
def get_all_words(request):
    word_ids = list(Word.objects.values_list('id', flat=True))
    random.shuffle(word_ids)
    words = [Word.objects.get(id=id).text for id in word_ids]
    return JsonResponse({'words': words})

@require_http_methods(["POST"])
def save_response(request):
    # Extract the user's response and the word id
    data = json.loads(request.body)
    word_text = data.get('word')
    user_input = data.get('response')
    duration = data.get('duration')

    # Save the response
    UserResponse.objects.create(word_text=word_text, user_input=user_input, duration=duration)
    return JsonResponse({'status': 'success'})
