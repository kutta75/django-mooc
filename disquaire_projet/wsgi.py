"""
WSGI config for disquaire_projet project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

path1= '/var/www/disquaire_projet/disquaire_projet/disquaire_projet'
if path1  not in  sys.path:
    sys.path.append(path1)
path2= '/var/www/disquaire_projet/disquaire_projet/store'
if path2  not in  sys.path:
    sys.path.append(path2)


#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "disquaire_projet.settings")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
application = get_wsgi_application()
