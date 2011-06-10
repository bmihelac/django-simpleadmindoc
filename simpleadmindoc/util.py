from django.db import models
from django.utils.translation import ugettext as _


def get_model(app_label, model_name):
    for model in models.get_models(models.get_app(app_label)):
        if model_name == model._meta.object_name:
            return model
    raise ValueError("Model %s.%s does not exist" % (app_label, model_name))

def model_attribute_name(app_label, model_name, attribute):
    model = get_model(app_label, model_name)
    name = model._meta.get_field_by_name(attribute)[0].verbose_name
    return name

def model_name(app_label, model_name, plural=False):
    model = get_model(app_label, model_name)
    name = model._meta.verbose_name_plural if plural else model._meta.verbose_name
    return name

def model_attributes(app_label, model_name):
    model = get_model(app_label, model_name)
    attributes = {}
    for field in model._meta.fields:
        attributes[field.name] = {
                'description': field.help_text
                }
    for field in model._meta.many_to_many:
        desc = _('Many to many relation with :djangoadmin:model:`%s.%s`.' % (
            field.rel.to._meta.app_label,
            field.rel.to._meta.object_name))
        attributes[field.name] = {
                'description': desc
                }
    return attributes
