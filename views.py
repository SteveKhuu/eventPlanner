'''
Created on Nov 13, 2012

@author: Stephen_Khuu
'''

from django.shortcuts import render

def index(request):
  return render(request, 'index.html')