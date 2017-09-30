from django.contrib import admin
from .models import Poll, Choice

class PollAdmin(admin.ModelAdmin):
    list_display = ['question', 'pub_date']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['poll']

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
