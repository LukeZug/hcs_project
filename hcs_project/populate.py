import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hcs_project.settings')

import django
django.setup()
from emoji_password_evaluation.models import Word

def populate():
    passwords = [{'text': 'password🥳lol'}, {'text': 'cantbereal%^%&😊😡'}, {'text': 'nowaythatstrue'}, {'text': 'password12345'}]
    for password in passwords:
        pwd = Word.objects.get_or_create(text=password.get('text'))

if __name__ == '__main__':
    populate()