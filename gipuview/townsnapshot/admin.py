from django.contrib import admin

# Register your models here.

from django.contrib import admin
from townsnapshot.models import Municipio
from townsnapshot.models import Tipo
from townsnapshot.models import Stats

admin.site.register(Municipio)
admin.site.register(Tipo)
admin.site.register(Stats)
