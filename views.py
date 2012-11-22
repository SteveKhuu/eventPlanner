'''
Created on Nov 13, 2012

@author: Stephen_Khuu
'''

import random

from django.cong import settings
from django.shortcuts import render
from eventPlanner.models import Events


def index(request):
  login_ctas = ['Got an awesome event? Log in and post it!', 
                'Need to organize an event? Log in and start here!', 
                'You\'re a login away from event planning bliss...',
                ]
  
  login_cta = login_ctas[random.randrange(0, len(login_ctas))]
  
  total_events = 0
  total_events_attending = 0
  total_events_attending_expired = 0
  
  if request.user.is_authenticated():
    
    total_events = Events.objects.count()
    
    events_attending = Events.objects.filter(attendees=request.user)
    total_events_attending = events_attending.count()
    
    for event in events_attending:
      if event.is_over():
        total_events_attending_expired += 1
  
  heroku_test = ''
  if settings.ON_HEROKU:
    heroku_test = '(on heroku)'
    
  context = {'login_cta' : login_cta,
             'total_events' : total_events,
             'total_events_attending' : total_events_attending,
             'total_events_attending_active' : (total_events_attending - total_events_attending_expired),
             'total_events_attending_expired' : total_events_attending_expired,
             'heroku_test' : heroku_test
             }
  return render(request, 'index.html', context)