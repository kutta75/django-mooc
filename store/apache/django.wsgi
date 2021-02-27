import os 
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

path = '/var/www/disquaire_projet/disquaire_projet/disquaire_projet'
if path not in sys.path:
	sys.path.append(path)
import django.core.handlers.wsgi
from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()
application = django.core.handlers.wsgi.WSGIHandler()

