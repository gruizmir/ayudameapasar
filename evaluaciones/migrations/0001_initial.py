# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PuntuacionAyudantes'
        db.create_table(u'evaluaciones_puntuacionayudantes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('puntaje', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('ayudantia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ayudantias.Ayudantia'])),
        ))
        db.send_create_signal(u'evaluaciones', ['PuntuacionAyudantes'])

        # Adding model 'PuntuacionAlumno'
        db.create_table(u'evaluaciones_puntuacionalumno', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('puntaje', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'evaluaciones', ['PuntuacionAlumno'])

        # Adding model 'MotivoAbuso'
        db.create_table(u'evaluaciones_motivoabuso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30L)),
        ))
        db.send_create_signal(u'evaluaciones', ['MotivoAbuso'])

        # Adding model 'ReporteAbusoAyudante'
        db.create_table(u'evaluaciones_reporteabusoayudante', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('motivo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['evaluaciones.MotivoAbuso'])),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('comentario', self.gf('django.db.models.fields.TextField')()),
            ('ayudante', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['usuarios.Ayudante'])),
            ('reportador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'evaluaciones', ['ReporteAbusoAyudante'])

        # Adding model 'ReporteAbusoAlumno'
        db.create_table(u'evaluaciones_reporteabusoalumno', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('motivo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['evaluaciones.MotivoAbuso'])),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('comentario', self.gf('django.db.models.fields.TextField')()),
            ('alumno', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('reportador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['usuarios.Ayudante'])),
        ))
        db.send_create_signal(u'evaluaciones', ['ReporteAbusoAlumno'])


    def backwards(self, orm):
        # Deleting model 'PuntuacionAyudantes'
        db.delete_table(u'evaluaciones_puntuacionayudantes')

        # Deleting model 'PuntuacionAlumno'
        db.delete_table(u'evaluaciones_puntuacionalumno')

        # Deleting model 'MotivoAbuso'
        db.delete_table(u'evaluaciones_motivoabuso')

        # Deleting model 'ReporteAbusoAyudante'
        db.delete_table(u'evaluaciones_reporteabusoayudante')

        # Deleting model 'ReporteAbusoAlumno'
        db.delete_table(u'evaluaciones_reporteabusoalumno')


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
        u'ayudantias.ayudantia': {
            'Meta': {'object_name': 'Ayudantia'},
            'ayudante': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['usuarios.Ayudante']"}),
            'categoria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ayudantias.Categoria']", 'null': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'estado': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fecha_publicacion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'subcategoria': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['ayudantias.Subcategoria']", 'null': 'True', 'blank': 'True'})
        },
        u'ayudantias.categoria': {
            'Meta': {'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50L'})
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
        u'evaluaciones.motivoabuso': {
            'Meta': {'object_name': 'MotivoAbuso'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30L'})
        },
        u'evaluaciones.puntuacionalumno': {
            'Meta': {'object_name': 'PuntuacionAlumno'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'puntaje': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'evaluaciones.puntuacionayudantes': {
            'Meta': {'object_name': 'PuntuacionAyudantes'},
            'ayudantia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ayudantias.Ayudantia']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'puntaje': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'evaluaciones.reporteabusoalumno': {
            'Meta': {'object_name': 'ReporteAbusoAlumno'},
            'alumno': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'comentario': ('django.db.models.fields.TextField', [], {}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'motivo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['evaluaciones.MotivoAbuso']"}),
            'reportador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['usuarios.Ayudante']"})
        },
        u'evaluaciones.reporteabusoayudante': {
            'Meta': {'object_name': 'ReporteAbusoAyudante'},
            'ayudante': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['usuarios.Ayudante']"}),
            'comentario': ('django.db.models.fields.TextField', [], {}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'motivo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['evaluaciones.MotivoAbuso']"}),
            'reportador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'usuarios.ayudante': {
            'Meta': {'object_name': 'Ayudante'},
            'eval_qty': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'puntuacion': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'usuario': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['evaluaciones']