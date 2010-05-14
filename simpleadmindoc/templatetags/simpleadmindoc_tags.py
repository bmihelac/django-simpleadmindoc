from django import template
from django.db import models
from django.core.urlresolvers import reverse

from simpleadmindoc.generate import get_model


register = template.Library()


@register.simple_tag
def field_definition(model_opts, field):
    s = []
    model_signature = '%s.%s' % (model_opts.app_label, model_opts.object_name)
    s.append('.. djangoadmin:attribute:: ' + model_signature + '.' + field.name + ' ' + unicode(field.verbose_name))
    s.append('')
    if field.help_text:
        s.append('\t' + unicode(field.help_text).strip())
        s.append('\t')
    if field.rel:
        field_type_description = ":djangoadmin:class:`%s.%s`" % (field.rel.to._meta.app_label, \
                                 field.rel.to._meta.object_name)
    else:
        field_type_description = field.description % field.__dict__
    s.append('\t' + field_type_description)
    return '\n'.join(s)

# TODO: filtering which fields to return: only, exclude, of_type
# TODO: in most cases we need only the fields that are visible in admin form and by that order
@register.inclusion_tag('simpleadmindoc/fields_for_model.rst', takes_context=True)
def fields_for_model(context, model_opts):
    all_fields = model_opts.fields
    m2m_fields = []
    for field in model_opts.many_to_many:
        all_fields.append(field)
    return {'fields': all_fields, 'model_opts': model_opts }
    
