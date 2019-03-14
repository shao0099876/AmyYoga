"""
WSGI config for AmyYoga project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append("/usr/local/lib/python3.7/site-packages")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AmyYoga.settings')

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
