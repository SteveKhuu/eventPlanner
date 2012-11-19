'''
Created on Nov 13, 2012

@author: Stephen_Khuu
'''

import icalendar
import random
from icalendar import Calendar, Event

from django import forms
from django.contrib.sites.models import Site
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.mail.message import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import slugify

from eventPlanner.models import Events, Attendee, Task

def index(request):
  latest_event_list = Events.objects.order_by('-start_datetime')[:5]
  
  expired_events = []
  active_events = []
  
  for event in latest_event_list:
    if event.is_over():
      expired_events.append(event)
    else:
      active_events.append(event)
  
  context = {'active_events': active_events,
             'expired_events': expired_events,
             'title': 'Events'}
  
  return render(request, 'events/index.html', context)

def my_events(request):
  user = request.user

  latest_event_list = Events.objects.filter(attendees=user).order_by('-start_datetime')[:5]
  
  expired_events = []
  active_events = []
  
  for event in latest_event_list:
    if event.is_over():
      expired_events.append(event)
    else:
      active_events.append(event)
      
  context = {'active_events': active_events,
             'expired_events': expired_events,
             'title': 'My Events'}

  return render(request, 'events/index.html', context)

def detail(request, event_id):
  
  event = get_object_or_404(Events, pk=event_id)
  attendees = event.attendees.all()
  is_attending = event.attendees.filter(username=request.user.username).exists()
  
  is_managing = False
  
  tasks = []
  
  if is_attending:
    attendee = Attendee.objects.get(event=event, user=request.user)
    is_managing = is_managing or attendee.is_managing
    
    if is_managing:
      tasks = Task.objects.filter(event=event)
    
  context = {'event' : event,
             'attendees' : attendees,
             'num_attendees' : attendees.count(),
             'is_attending' : is_attending,
             'is_managing' : is_managing, 
             'tasks' : tasks
             }
  return render(request, 'events/detail.html', context)

def update(request, event_id):
  event = get_object_or_404(Events, pk=event_id)
  return render(request, 'events/detail.html', {'event': event})

def attend(request, event_id):
  event = get_object_or_404(Events, pk=event_id)
  
  attendee, created = Attendee.objects.get_or_create(event=event, user=request.user)
  
  if created:
    attendee.save()
  
  return redirect('detail', event_id=event_id)

def leave(request, event_id):
  event = get_object_or_404(Events, pk=event_id)
  
  attendee = Attendee.objects.get(event=event, user=request.user)
  
  attendee.delete()
  
  return redirect('detail', event_id=event_id)

def make_calendar_object(event_id):
  event = get_object_or_404(Events, pk=event_id)

  site = Site.objects.get_current()

  site_token = site.domain.split('.')
  site_token.reverse()
  site_token = '.'.join(site_token)
  
  cal = Calendar()
  cal.add('prodid', '-//%s Events Calendar//%s//' % (site.name, site.domain))
  cal.add('version', '2.0')

  eventObj = Event()
  eventObj.add('summary', event.name)
  eventObj.add('location', event.location)
  eventObj.add('dtstart', event.start_datetime)
  eventObj.add('dtend', event.end_datetime)
  eventObj.add('dtstamp', event.created_datetime)
  eventObj['uid'] = '%dT%d.events.%s' % (event.id, random.randrange(111111111,999999999), site_token)
  eventObj.add('priority', 5)

  cal.add_component(eventObj)

  output = ""
  for line in cal.content_lines():
    if line:
      output += line + "\n"
  
  return output

def export(request, event_id):
  event = get_object_or_404(Events, pk=event_id)
  output = make_calendar_object(event_id)
  
  response = HttpResponse(output, mimetype="text/calendar")
  response['Content-Disposition'] = 'attachment; filename=%s.ics' % slugify(event.name + "-" + str(event.start_datetime.year))
  return response

def send_email(request, event_id):
  event = get_object_or_404(Events, pk=event_id)
  output = make_calendar_object(event_id)
  
  attachment_name = '%s.ics' % slugify(event.name + "-" + str(event.start_datetime.year))
  
  context = {'event': event,
             'title' : 'Uh-oh!',
             'message' : 'Something went wrong when sending out the invitation'}
    
  try:
    mail = EmailMessage(event.name, event.description, 'Stephen_Khuu@epam.com', ['Stephen_Khuu@epam.com'])#['Tom_Klimovski@epam.com', 'Osman_Ishaq@epam.com', 'Frank_Vanderzwet@epam.com', 'Stephen_Khuu@epam.com'])
    mail.attach(attachment_name, output, 'text/calendar')
    mail.send()
  
    event.flag_submitted()
            
    context['title'] = 'Success!'
    context['message'] = 'Invitation was successfully sent!'
    return render(request, 'events/send_done.html', context)
  except:
    context['title'] = 'Error!'
    context['message'] = 'There was an error sending your invitation.'
    return render(request, 'events/send_done.html', context)
  
  return render(request, 'events/send_done.html', context)
