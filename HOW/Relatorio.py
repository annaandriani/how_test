import django
django.setup()
import os
import django
import sys




sys.path.append( "/mysite/settings.py" )

BASE_DIR = os.path.dirname(os.path.mysite(os.path.abspath(settings)))
    sys.path.append(HOW_Assist)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()


from django.db import models

class Pessoa(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name