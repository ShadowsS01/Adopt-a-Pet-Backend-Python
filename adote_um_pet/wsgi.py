import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "adote_um_pet.settings")

application = get_wsgi_application()
