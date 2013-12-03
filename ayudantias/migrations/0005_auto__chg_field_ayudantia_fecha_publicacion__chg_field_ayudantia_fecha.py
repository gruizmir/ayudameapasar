# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Ayudantia.fecha_publicacion'
        db.alter_column(u'ayudantias_ayudantia', 'fecha_publicacion', self.gf('django.db.models.fields.DateField')(auto_now_add=True))

        # Changing field 'Ayudantia.fecha_termino'
        db.alter_column(u'ayudantias_ayudantia', 'fecha_termino', self.gf('django.db.models.fields.DateField')())

        # Changing field 'AlumnoAyudantia.fecha_solicitud'
        db.alter_column(u'ayudantias_alumnoayudantia', 'fecha_solicitud', self.gf('django.db.models.fields.DateField')(auto_now_add=True))

    def backwards(self, orm):

        # Changing field 'Ayudantia.fecha_publicacion'
        db.alter_column(u'ayudantias_ayudantia', 'fecha_publicacion', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

        # Changing field 'Ayudantia.fecha_termino'
        db.alter_column(u'ayudantias_ayudantia', 'fecha_termino', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'AlumnoAyudantia.fecha_solicitud'
        db.alter_column(u'ayudantias_alumnoayudantia', 'fecha_solicitud', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'ayudantias.alumnoayudantia': {
            'Meta': {'object_name': 'AlumnoAyudantia'},
            'aceptada': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'alumno': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'asistio': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ayudantia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ayudantias.Ayudantia']"}),
            'cantidad_personas': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'fecha_solicitud': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'horario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ayudantias.HorarioAyudantia']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'ayudantias.ayudantia': {
            'Meta': {'object_name': 'Ayudantia'},
            'ayudante': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['usuarios.Ayudante']"}),
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ayudantias.Categoria']", 'null': 'True', 'blank': 'True'}),
            'costo_por_hora': ('django.db.models.fields.IntegerField', [], {}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'estado': ('django.db.models.fields.CharField', [], {'default': "u'1'", 'max_length': '1'}),
            'fecha_publicacion': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_termino': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'subcategoria': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['ayudantias.Subcategoria']", 'null': 'True', 'blank': 'True'})
        },
        u'ayudantias.categoria': {
            'Meta': {'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50L'})
        },
        u'ayudantias.horarioayudantia': {
            'Meta': {'object_name': 'HorarioAyudantia'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'ayudantia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ayudantias.Ayudantia']"}),
            'dia': ('django.db.models.fields.CharField', [], {'default': "u'1'", 'max_length': '1'}),
            'hora_final': ('django.db.models.fields.TimeField', [], {}),
            'hora_inicio': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'ayudantias.subcategoria': {
            'Meta': {'object_name': 'Subcategoria'},
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ayudantias.Categoria']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50L'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'usuarios.ayudante': {
            'Meta': {'object_name': 'Ayudante'},
            'eval_qty': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'puntuacion': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'usuario': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['ayudantias']