# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'project_project', (
            ('project_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=400)),
            ('money_req', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('days_req', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('video_link', self.gf('django.db.models.fields.URLField')(max_length=1000)),
            ('details', self.gf('django.db.models.fields.TextField')(max_length=4000)),
            ('project_use', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('risks_and_challenges', self.gf('django.db.models.fields.TextField')(max_length=4000)),
            ('number_of_options', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('pledge_value', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('pledge_reward', self.gf('django.db.models.fields.TextField')(max_length=8000)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'project', ['Project'])

        # Adding model 'Pledger'
        db.create_table(u'project_pledger', (
            ('pid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pledger', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pledger_user_id', to=orm['auth.User'])),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pledge_project_id', to=orm['project.Project'])),
            ('amount_pledged', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'project', ['Pledger'])

        # Adding model 'ProjectUpdate'
        db.create_table(u'project_projectupdate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')(max_length=4000)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('project_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['project.Project'])),
        ))
        db.send_create_signal(u'project', ['ProjectUpdate'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'project_project')

        # Deleting model 'Pledger'
        db.delete_table(u'project_pledger')

        # Deleting model 'ProjectUpdate'
        db.delete_table(u'project_projectupdate')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'project.pledger': {
            'Meta': {'object_name': 'Pledger'},
            'amount_pledged': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pledger': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pledger_user_id'", 'to': u"orm['auth.User']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pledge_project_id'", 'to': u"orm['project.Project']"})
        },
        u'project.project': {
            'Meta': {'object_name': 'Project'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'days_req': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '400'}),
            'details': ('django.db.models.fields.TextField', [], {'max_length': '4000'}),
            'money_req': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'number_of_options': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'pledge_reward': ('django.db.models.fields.TextField', [], {'max_length': '8000'}),
            'pledge_value': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'project_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project_use': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'risks_and_challenges': ('django.db.models.fields.TextField', [], {'max_length': '4000'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'video_link': ('django.db.models.fields.URLField', [], {'max_length': '1000'})
        },
        u'project.projectupdate': {
            'Meta': {'object_name': 'ProjectUpdate'},
            'content': ('django.db.models.fields.TextField', [], {'max_length': '4000'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['project.Project']"})
        }
    }

    complete_apps = ['project']