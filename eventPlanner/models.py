import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from datetime import datetime

class Events(models.Model):
  
  class Meta:
    verbose_name_plural = "Events"
    
  EVENT_STATUS = (
      ('DR', 'Draft'),
      ('SB', 'Submitted'),
  )
  
  name = models.CharField(max_length=200)
  location = models.CharField(max_length=1000)
  description = models.TextField()
  status = models.CharField(max_length=2, choices=EVENT_STATUS, default='DR')
  start_datetime = models.DateTimeField('start datetime')
  end_datetime = models.DateTimeField('end datetime')
  created_datetime = models.DateTimeField(default=datetime.now)
  
  attendees = models.ManyToManyField(User, through='Attendee')
  
  def flag_submitted(self):
    self.status = 'SB'
    self.save()
    
  def is_over(self):
    return timezone.now() >= self.end_datetime
  is_over.admin_order_field = 'start_datetime'
  is_over.boolean = True
  is_over.short_description = 'Is the event over?'
  
  def was_published_recently(self):
    return self.created_datetime >= timezone.now() - datetime.timedelta(days=1)
  was_published_recently.admin_order_field = 'created_datetime'
  was_published_recently.boolean = True
  was_published_recently.short_description = 'Published recently?'
        
  def __unicode__(self):
    return self.name

class Attendee(models.Model):
  user = models.ForeignKey(User)
  event = models.ForeignKey(Events)
  is_managing = models.BooleanField(default=False)
  
  def __unicode__(self):
    return unicode(self.user.username) + " => " + unicode(self.event.name)

class Task(models.Model):
  name = models.CharField(max_length=200)
  user = models.ForeignKey(User)
  event = models.ForeignKey(Events)
  complete = models.BooleanField(default=False)
  target_datetime = models.DateTimeField('do task by', blank=True, null=True)
  
  def __unicode__(self):
    return self.name

class Comment(models.Model):
  user = models.ForeignKey(User)
  event = models.ForeignKey(Events)
  comment = models.CharField(max_length=1000)
  created_datetime = models.DateTimeField(default=datetime.now)
  
  def __unicode__(self):
    return self.event.name + ": " + self.comment
  