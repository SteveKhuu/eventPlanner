# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Event'
        db.delete_table('eventPlanner_event')

        # Adding model 'Events'
        db.create_table('eventPlanner_events', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eventPlanner.Category'], null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='DR', max_length=2)),
            ('start_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('created_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('eventPlanner', ['Events'])

        # Adding model 'Category'
        db.create_table('eventPlanner_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('eventPlanner', ['Category'])


    def backwards(self, orm):
        # Adding model 'Event'
        db.create_table('eventPlanner_event', (
            ('start_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('created_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('end_datetime', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('eventPlanner', ['Event'])

        # Deleting model 'Events'
        db.delete_table('eventPlanner_events')

        # Deleting model 'Category'
        db.delete_table('eventPlanner_category')


    models = {
        'eventPlanner.attendee': {
            'Meta': {'object_name': 'Attendee'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'eventPlanner.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'eventPlanner.events': {
            'Meta': {'object_name': 'Events'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['eventPlanner.Category']", 'null': 'True', 'blank': 'True'}),
            'created_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'start_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'DR'", 'max_length': '2'})
        }
    }

    complete_apps = ['eventPlanner']