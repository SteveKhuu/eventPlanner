'''
Created on Nov 13, 2012

@author: Stephen_Khuu
'''

import random
from django.shortcuts import render


def index(request):
  login_ctas = ['Got an awesome event? Log in and post it!', 
                'Need to organize an event? Log in and start here!', 
                'You\'re a login away from event planning bliss...',
                ]
  
  login_cta = login_ctas[random.randrange(0, len(login_ctas))]
  
  
  context = {'login_cta' : login_cta
             }
  return render(request, 'index.html', context)