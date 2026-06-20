from django.contrib import admin

from .models import Sensor, Sample

admin.site.register(Sensor)
admin.site.register(Sample)
