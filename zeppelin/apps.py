from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class ZeppelinConfig(AppConfig):
    name = 'zeppelin'
    verbose_name="Leds Zeppelin"
    
    def ready(self):
        from . import signals