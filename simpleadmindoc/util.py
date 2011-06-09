from django.db import models


def model_attribute_name(app_label, model_name, attribute):
    app_models = models.get_models(models.get_app(app_label))
    model = app_models[[m._meta.object_name for m in app_models].index(model_name)]
    name = model._meta.get_field_by_name(attribute)[0].verbose_name
    return name

def model_name(app_label, model_name, plural=False):
    app_models = models.get_models(models.get_app(app_label))
    model = app_models[[m._meta.object_name for m in app_models].index(model_name)]
    name = model._meta.verbose_name_plural if plural else model._meta.verbose_name
    return name

def get_model(app_label, model_name):
    app_models = models.get_models(models.get_app(app_label))
    return app_models[[m._meta.object_name.lower() for m in app_models].index(model_name)]
