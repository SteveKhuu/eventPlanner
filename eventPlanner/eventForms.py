'''
Created on Nov 19, 2012

@author: Stephen_Khuu
'''
from django.forms import ModelForm
from eventPlanner.models import Events, Attendee, Task
from eventPlanner.widgets import SplitSelectDateTimeWidget

class EventForm(ModelForm):
    class Meta:
      model = Events
      fields = ('name', 'location', 'description', 'start_datetime', 'end_datetime')
      widgets = {
        'start_datetime' : SplitSelectDateTimeWidget(),
        'end_datetime' : SplitSelectDateTimeWidget()
      }