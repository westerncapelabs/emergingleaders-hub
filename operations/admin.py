from django.contrib import admin
from django_tablib.admin import TablibAdmin
from leaflet.admin import LeafletGeoAdmin
from .models import Trainer, Participant, Location


class TrainerAdmin(TablibAdmin):
    list_display = ('name', 'msisdn', 'email', 'extras', 'created_at',
                    'updated_at')
    list_filter = ['name', 'msisdn', 'email', 'extras', 'created_at',
                   'updated_at']
    search_fields = ['name', 'msisdn', 'email']
    formats = ['xls', 'csv']


class ParticipantAdmin(TablibAdmin):
    list_display = ('msisdn', 'lang', 'full_name', 'gender', 'id_type',
                    'id_no', 'dob', 'passport_origin', 'created_at',
                    'updated_at')
    list_filter = ['msisdn', 'lang', 'full_name', 'gender', 'id_type',
                   'id_no', 'dob', 'passport_origin', 'created_at',
                   'updated_at']
    search_fields = ['msisdn', 'full_name']
    formats = ['xls', 'csv']


admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Location, LeafletGeoAdmin)
