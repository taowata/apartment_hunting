from django.core.management.utils import get_random_secret_key

secret_key = get_random_secret_key()
text = "SECRET_KEY = '{}'\n".format(secret_key)
file = open('local_settings.py', 'w', encoding='UTF-8')

file.write(text)
