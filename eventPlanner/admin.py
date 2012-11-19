'''
Created on Nov 13, 2012

@author: Stephen_Khuu
'''

from django.contrib import admin
from eventPlanner.models import Events, Task, Attendee

class EventsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic information',               {'fields': ['name', 'status', 'location', 'description']}),
        ('Date information', {'fields': ['start_datetime', 'end_datetime']}),
    ]
    list_display = ('name', 'status', 'is_over', 'location', 'start_datetime')
    list_filter = ['start_datetime']
    date_hierarchy = 'start_datetime'

class AttendeeAdmin(admin.ModelAdmin):
  list_display = ('user', 'event', 'is_managing')
  
class TaskAdmin(admin.ModelAdmin):
  list_display = ('user', 'event', 'complete', 'target_datetime')
  list_filter = ['target_datetime']
  date_hierarchy = 'target_datetime'
    
admin.site.register(Events, EventsAdmin)
admin.site.register(Attendee, AttendeeAdmin)
admin.site.register(Task, TaskAdmin)
