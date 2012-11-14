'''
Created on Nov 13, 2012

@author: Stephen_Khuu
'''

import icalendar
import random
from icalendar import Calendar, Event

from django.contrib.sites.models import Site
from django.core.mail.message import EmailMessage

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import slugify

from eventPlanner.models import Events

def index(request):
  latest_event_list = Events.objects.order_by('-start_datetime')[:5]
  context = {'latest_event_list': latest_event_list}
  return render(request, 'events/index.html', context)
#  return HttpResponse("Hello, world. You're at the event planner index.")
  
def detail(request, event_id):
  event = get_object_or_404(Events, pk=event_id)
  return render(request, 'events/detail.html', {'event': event})

def update(request, event_id):
  event = get_object_or_404(Events, pk=event_id)
  return render(request, 'events/detail.html', {'event': event})

def attend(request, event_id):
  return HttpResponse("You're attending event %s." % event_id)

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
