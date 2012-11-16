from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eventPlanner.views.home', name='home'),
    # url(r'^eventPlanner/', include('eventPlanner.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    url(r'^$', views.index, name='home'),
    
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/profile/', redirect_to, {'url': '/events/'}),
    
    url(r'^events/', include('eventPlanner.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
)

