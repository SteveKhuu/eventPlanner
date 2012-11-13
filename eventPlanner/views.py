'''
Created on Nov 13, 2012

@author: Stephen_Khuu
'''
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the event planner index.")