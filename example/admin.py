from django.contrib import admin
from models import Position


class PositionAdmin(admin.ModelAdmin):
    list_display = ['lat', 'lng']

admin.site.register(Position, PositionAdmin)