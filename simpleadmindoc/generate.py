import os, os.path

from django.db import models
from django.template import Context, Template
from django.template.loader import select_template
from django.core.exceptions import ImproperlyConfigured

from django.conf import settings


SIMPLEADMINDOC_PATH = getattr(settings, 'SIMPLEADMINDOC_PATH', "docs")

def write(filename, content):
    pathname = os.path.split(filename)[0]
    if not os.path.exists(pathname):
        os.makedirs(pathname)
    f = open(filename, "w")
    f.write(content.encode('utf-8'))
    f.close()
    
def get_model(app_label, model_name):
    try:
        app_models = models.get_models(models.get_app(app_label))
        return app_models[[m._meta.object_name.lower() for m in app_models].index(model_name)]
    except (ValueError, ImproperlyConfigured), e:
        raise NameError('Could not find model: %s in app: %s' % (app_label, model_name))

def model_doc(model):
    ctx = Context()
    ctx['opts'] = model._meta
    templates = ('simpleadmindoc/%s/%s.rst' % (model._meta.app_label, model.__name__.lower()), 
                'simpleadmindoc/%s/model.rst' % model._meta.app_label, 
                'simpleadmindoc/model.rst')
    tmpl = select_template(templates)
    return tmpl.render(ctx)


def generate_model_doc(model):
    content = model_doc(model)
    filename = '%s/apps/%s/%s.rst' % (SIMPLEADMINDOC_PATH, model._meta.app_label, model.__name__.lower())
    write(filename, content)
    
def app_doc(app):
    app_label = app.__name__.split('.')[-2]
    ctx = Context()
    ctx['app_label'] = app_label
    templates = ('simpleadmindoc/%s/app.rst' % app_label, 
                'simpleadmindoc/app.rst')
    tmpl = select_template(templates)
    return tmpl.render(ctx)

def generate_app_doc(app):
    app_label = app.__name__.split('.')[-2]
    content = app_doc(app)
    filename = '%s/apps/%s/app.rst' % (SIMPLEADMINDOC_PATH, app_label)
    write(filename, content)
    
def index_doc():
    ctx = Context()
    templates = ('simpleadmindoc/index.rst', )
    tmpl = select_template(templates)
    return tmpl.render(ctx)    
    
def generate_index_doc():
    filename = '%s/index.rst' % (SIMPLEADMINDOC_PATH,)
    content = index_doc()
    write(filename, content)    