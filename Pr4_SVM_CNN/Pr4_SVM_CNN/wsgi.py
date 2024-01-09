
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pr4_SVM_CNN.settings")

application = get_wsgi_application()
