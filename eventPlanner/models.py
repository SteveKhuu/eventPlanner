import datetime
from django.utils import timezone
from django.db import models

from datetime import datetime

class Event(models.Model):
  name = models.CharField(max_length=200)
  location = models.CharField(max_length=1000)
  description = models.TextField()
  start_datetime = models.DateTimeField('start datetime')
  end_datetime = models.DateTimeField('end datetime')
  created_datetime = models.DateTimeField(default=datetime.now)
    
  def was_published_recently(self):
    return self.created_datetime >= timezone.now() - datetime.timedelta(days=1)
      
  def __unicode__(self):
    return self.name
    
class Attendee(models.Model):
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  
  def __unicode__(self):
    return self.first_name + " " + self.last_name
  