"""
WSGI config for puppersupperdev project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'puppersupperdev.settings')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "puppersupperdev/credentials/DogFit.json"


application = get_wsgi_application()
