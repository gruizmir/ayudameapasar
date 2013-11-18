# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Region'
        db.create_table(u'main_region', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30L, blank=True)),
        ))
        db.send_create_signal(u'main', ['Region'])

        # Adding model 'Ciudad'
        db.create_table(u'main_ciudad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100L, blank=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Region'], null=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['Ciudad'])

        # Adding model 'Institucion'
        db.create_table(u'main_institucion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60L)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Region'], null=True, blank=True)),
            ('ciudad', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['main.Ciudad'], null=True, blank=True)),
        ))
        db.send_create_signal(u'main', ['Institucion'])

        # Adding model 'EmailValidos'
        db.create_table(u'main_emailvalidos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dominio', self.gf('django.db.models.fields.CharField')(max_length=20L)),
            ('institucion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Institucion'])),
        ))
        db.send_create_signal(u'main', ['EmailValidos'])


    def backwards(self, orm):
        # Deleting model 'Region'
        db.delete_table(u'main_region')

        # Deleting model 'Ciudad'
        db.delete_table(u'main_ciudad')

        # Deleting model 'Institucion'
        db.delete_table(u'main_institucion')

        # Deleting model 'EmailValidos'
        db.delete_table(u'main_emailvalidos')


    models = {
        u'main.ciudad': {
            'Meta': {'object_name': 'Ciudad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Region']", 'null': 'True', 'blank': 'True'})
        },
        u'main.emailvalidos': {
            'Meta': {'object_name': 'EmailValidos'},
            'dominio': ('django.db.models.fields.CharField', [], {'max_length': '20L'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Institucion']"})
        },
        u'main.institucion': {
            'Meta': {'object_name': 'Institucion'},
            'ciudad': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['main.Ciudad']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60L'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Region']", 'null': 'True', 'blank': 'True'})
        },
        u'main.region': {
            'Meta': {'object_name': 'Region'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30L', 'blank': 'True'})
        }
    }

    complete_apps = ['main']