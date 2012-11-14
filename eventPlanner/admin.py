'''
Created on Nov 13, 2012

@author: Stephen_Khuu
'''

from django.contrib import admin
from eventPlanner.models import Category
from eventPlanner.models import Event
#from eventPlanner.models import Attendee

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic information',               {'fields': ['name', 'category', 'status', 'location', 'description']}),
        ('Date information', {'fields': ['start_datetime', 'end_datetime']}),
    ]
    list_display = ('name', 'status', 'is_over', 'category', 'location', 'start_datetime')
    list_filter = ['start_datetime']
    date_hierarchy = 'start_datetime'
    
admin.site.register(Event, EventAdmin)
admin.site.register(Category)
#admin.site.register(Attendee)