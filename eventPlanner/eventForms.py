'''
Created on Nov 19, 2012

@author: Stephen_Khuu
'''
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django.forms.widgets import HiddenInput, Textarea
from eventPlanner.models import Events, Attendee, Task, Comment
from eventPlanner.widgets import SplitSelectDateTimeWidget

class EventForm(ModelForm):
    class Meta:
      model = Events
      fields = ('name', 'location', 'description', 'start_datetime', 'end_datetime')
      widgets = {
        'start_datetime' : SplitSelectDateTimeWidget(),
        'end_datetime' : SplitSelectDateTimeWidget()
      }
      
class CommentForm(ModelForm):
  
    comment = forms.CharField(widget=forms.Textarea, label='')
    
    class Meta:
      model = Comment
      fields = ('user', 'event', 'comment')
      widgets = {
        'event' : HiddenInput(),
        'user' : HiddenInput(),
      }
      
class TaskForm(ModelForm):
    
    class Meta:
      model = Task
      widgets = {
        'target_datetime' : HiddenInput()
      }
      
      
AddTaskFormset = inlineformset_factory(Events, Task, form=TaskForm, extra=1, can_delete=False)