from django.contrib import admin
from .models import Tournament, Winners, StaffEntry

# Register your models here.
admin.site.register(Tournament)
admin.site.register(Winners)
admin.site.register(StaffEntry)
