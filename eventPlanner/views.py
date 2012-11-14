'''
Created on Nov 13, 2012

@author: Stephen_Khuu
'''
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from eventPlanner.models import Event

def index(request):
  latest_event_list = Event.objects.order_by('-start_datetime')[:5]
  context = {'latest_event_list': latest_event_list}
  return render(request, 'events/index.html', context)
#  return HttpResponse("Hello, world. You're at the event planner index.")
  
def detail(request, event_id):
  event = get_object_or_404(Event, pk=event_id)
  return render(request, 'events/detail.html', {'event': event})

def update(request, event_id):
  event = get_object_or_404(Event, pk=event_id)
  return render(request, 'events/detail.html', {'event': event})

def attend(request, event_id):
  return HttpResponse("You're attending event %s." % event_id)
