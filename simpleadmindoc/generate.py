import os, os.path

from django.template import Context
from django.template.loader import select_template


SIMPLEADMINDOC_PATH = "docs"

def write(filename, content):
    pathname = os.path.split(filename)[0]
    if not os.path.exists(pathname):
        os.makedirs(pathname)
    f = open(filename, "w")
    f.write(content.encode('utf-8'))
    f.close()

def model_doc(model):
    ctx = Context()
    ctx['opts'] = model._meta
    templates = ('simpleadmindoc/%s/%s.rst' % (model._meta.app_label,
        model.__name__.lower()),
                'simpleadmindoc/%s/model.rst' % model._meta.app_label, 
                'simpleadmindoc/model.rst')
    tmpl = select_template(templates)
    return tmpl.render(ctx)


def generate_model_doc(model, path=None):
    content = model_doc(model)
    filename = '%s/%s/%s.rst' % (path or SIMPLEADMINDOC_PATH,
            model._meta.app_label, model.__name__.lower())
    write(filename, content)

def app_doc(app):
    app_label = app.__name__.split('.')[-2]
    ctx = Context()
    ctx['app_label'] = app_label
    templates = ('simpleadmindoc/%s/app.rst' % app_label,
                'simpleadmindoc/app.rst')
    tmpl = select_template(templates)
    return tmpl.render(ctx)

def generate_app_doc(app, path=None):
    app_label = app.__name__.split('.')[-2]
    content = app_doc(app)
    filename = '%s/%s/index.rst' % (path or SIMPLEADMINDOC_PATH, app_label)
    write(filename, content)

