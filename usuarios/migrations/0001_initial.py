# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Perfil'
        db.create_table(u'usuarios_perfil', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('institucion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['main.Institucion'], null=True, blank=True)),
            ('avatar', self.gf('django.db.models.fields.files.ImageField')(default=u'/static/img/profile_picture.png', max_length=100, blank=True)),
            ('puntuacion', self.gf('django.db.models.fields.FloatField')(default=0.0, blank=True)),
            ('eval_qty', self.gf('django.db.models.fields.IntegerField')(default=0, blank=True)),
            ('fono', self.gf('django.db.models.fields.CharField')(max_length=15L, null=True, blank=True)),
            ('es_ayudante', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'usuarios', ['Perfil'])

        # Adding model 'Ayudante'
        db.create_table(u'usuarios_ayudante', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('puntuacion', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('eval_qty', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'usuarios', ['Ayudante'])

        # Adding model 'InfoAcademica'
        db.create_table(u'usuarios_infoacademica', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ayudante', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['usuarios.Ayudante'])),
            ('nombre_ramo', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('carrera', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('tpo_experiencia', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'usuarios', ['InfoAcademica'])

        # Adding model 'AnuncioGeneral'
        db.create_table(u'usuarios_anunciogeneral', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('mensaje', self.gf('django.db.models.fields.TextField')()),
            ('enviar_email', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hora_publicacion', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('autor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'usuarios', ['AnuncioGeneral'])

        # Adding model 'UsuarioPorConfirmar'
        db.create_table(u'usuarios_usuarioporconfirmar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=150L)),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'usuarios', ['UsuarioPorConfirmar'])


    def backwards(self, orm):
        # Deleting model 'Perfil'
        db.delete_table(u'usuarios_perfil')

        # Deleting model 'Ayudante'
        db.delete_table(u'usuarios_ayudante')

        # Deleting model 'InfoAcademica'
        db.delete_table(u'usuarios_infoacademica')

        # Deleting model 'AnuncioGeneral'
        db.delete_table(u'usuarios_anunciogeneral')

        # Deleting model 'UsuarioPorConfirmar'
        db.delete_table(u'usuarios_usuarioporconfirmar')


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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'main.ciudad': {
            'Meta': {'object_name': 'Ciudad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100L', 'blank': 'True'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Region']", 'null': 'True', 'blank': 'True'})
        },
        u'main.institucion': {
            'Meta': {'object_name': 'Institucion'},
            'ciudad': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['main.Ciudad']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60L'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Region']"})
        },
        u'main.region': {
            'Meta': {'object_name': 'Region'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30L', 'blank': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '2L', 'blank': 'True'})
        },
        u'usuarios.anunciogeneral': {
            'Meta': {'object_name': 'AnuncioGeneral'},
            'autor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'enviar_email': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hora_publicacion': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mensaje': ('django.db.models.fields.TextField', [], {}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '50L'})
        },
        u'usuarios.ayudante': {
            'Meta': {'object_name': 'Ayudante'},
            'eval_qty': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'puntuacion': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'usuario': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'usuarios.infoacademica': {
            'Meta': {'object_name': 'InfoAcademica'},
            'ayudante': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['usuarios.Ayudante']"}),
            'carrera': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_ramo': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'tpo_experiencia': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'usuarios.perfil': {
            'Meta': {'object_name': 'Perfil'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'default': "u'/static/img/profile_picture.png'", 'max_length': '100', 'blank': 'True'}),
            'es_ayudante': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'eval_qty': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'fono': ('django.db.models.fields.CharField', [], {'max_length': '15L', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institucion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['main.Institucion']", 'null': 'True', 'blank': 'True'}),
            'puntuacion': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'usuarios.usuarioporconfirmar': {
            'Meta': {'object_name': 'UsuarioPorConfirmar'},
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '150L'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['usuarios']