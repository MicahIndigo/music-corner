"""
WSGI config for Music Corner project.


It exposes the WSGI callable as a module-level variable named ``application``.


This file is used by production WSGI servers such as Gunicorn.
"""


import os


from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGI_SETTINGS_MODULE", "musiccorner.settings")


application = get_wsgi_application()
