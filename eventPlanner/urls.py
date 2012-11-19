'''
Created on Nov 13, 2012

@author: Stephen_Khuu
'''
from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
from eventPlanner import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eventPlanner.views.home', name='home'),
    # url(r'^eventPlanner/', include('eventPlanner.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^my/$', views.my_events, name='my_events'),
    url(r'^(?P<event_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<event_id>\d+)/update$', views.update, name='update'),
    url(r'^(?P<event_id>\d+)/attend/$', views.attend, name='attend'),
    url(r'^(?P<event_id>\d+)/leave/$', views.leave, name='leave'),
    url(r'^(?P<event_id>\d+)/export/$', views.export, name='ics_export'),
    url(r'^(?P<event_id>\d+)/send_event/$', views.send_email, name='send_invite'),
)


