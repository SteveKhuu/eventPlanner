# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Task'
        db.delete_table('eventPlanner_task')

        # Deleting model 'Attendee'
        db.delete_table('eventPlanner_attendee')


    def backwards(self, orm):
        # Adding model 'Task'
        db.create_table('eventPlanner_task', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_managing', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('target_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eventPlanner.Events'])),
        ))
        db.send_create_signal('eventPlanner', ['Task'])

        # Adding model 'Attendee'
        db.create_table('eventPlanner_attendee', (
            ('is_managing', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['eventPlanner.Events'], null=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('eventPlanner', ['Attendee'])


    models = {
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