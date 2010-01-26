from django import template
from django.db import models
from django.core.urlresolvers import reverse


register = template.Library()


@register.inclusion_tag('simpleadmindoc/models_for_app.html', takes_context=True)
def models_for_app(context, app_label):
    app = models.get_app(app_label)
    all_models = [{'name': model._meta.verbose_name, 'link': reverse('simpleadmindoc-model-details', 
                args=(model._meta.app_label, model._meta.module_name)
                )} for model in models.get_models(app)]
    return {'all_models': all_models, 'name': app_label}