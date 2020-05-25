from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    pass

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass
