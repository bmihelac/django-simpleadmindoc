from django.db import models
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import Http404
from django.utils.translation import ugettext as _
from django.core.exceptions import ImproperlyConfigured
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.safestring import mark_safe
from django.core import urlresolvers


def doc_index(request):
    context = RequestContext(request)
    context['app_labels'] = set([model._meta.app_label for model in models.get_models()])
    return render_to_response('simpleadmindoc/index.html', 
        context_instance=context)
doc_index = staff_member_required(doc_index)


def model_detail(request, app_label, model_name):
    context = RequestContext(request)
    # Get the model class.
    try:
        app_mod = models.get_app(app_label)
    except ImproperlyConfigured:
        raise Http404(_("App %r not found") % app_label)
    model = None
    for m in models.get_models(app_mod):
        if m._meta.object_name.lower() == model_name:
            model = m
            break
    if model is None:
        raise Http404(_("Model %(model_name)r not found in app %(app_label)r") % {'model_name': model_name, 'app_label': app_label})
    
    opts = model._meta
    context['opts'] = opts
    
    # Gather fields/field descriptions.
    fields = []
    for field in opts.fields:
        # ForeignKey is a special case since the field will actually be a
        # descriptor that returns the other object
        if isinstance(field, models.ForeignKey):
            doc_link = urlresolvers.reverse('simpleadmindoc-model-details', 
                        args=(field.rel.to._meta.app_label, field.rel.to._meta.module_name)
                        )
            data_type = mark_safe('<a href="%s">%s</a>' % (doc_link,
                        field.description % field.__dict__))
            
        else:
            data_type = field.description % field.__dict__
        fields.append({
            'name': field.name,
            'data_type': data_type,
            'verbose': field.verbose_name,
            'help_text': field.help_text,
        })
    context['fields'] = fields
    
    # Gather many-to-many fields.
    m2m_fields = []
    for field in opts.many_to_many:
        doc_link = urlresolvers.reverse('simpleadmindoc-model-details', 
                    args=(field.rel.to._meta.app_label, field.rel.to._meta.module_name)
                    )
        data_type = mark_safe('<a href="%s">%s</a>' % (doc_link,
                    field.description % field.__dict__))
        m2m_fields.append({
            'name': field.name,
            "data_type": data_type,
            'verbose': field.rel.to._meta.verbose_name_plural,
            'help_text': field.help_text,
        })
    context['m2m_fields'] = m2m_fields
    
    templates = ('simpleadmindoc/%s/%s.html' % (app_label, model_name), 
                'simpleadmindoc/model_detail.html')
    return render_to_response(templates, context_instance=context)

    # 

    # 
    # # Gather model methods.
    # for func_name, func in model.__dict__.items():
    #     if (inspect.isfunction(func) and len(inspect.getargspec(func)[0]) == 1):
    #         try:
    #             for exclude in MODEL_METHODS_EXCLUDE:
    #                 if func_name.startswith(exclude):
    #                     raise StopIteration
    #         except StopIteration:
    #             continue
    #         verbose = func.__doc__
    #         if verbose:
    #             verbose = utils.parse_rst(utils.trim_docstring(verbose), 'model', _('model:') + opts.module_name)
    #         fields.append({
    #             'name': func_name,
    #             'data_type': get_return_data_type(func_name),
    #             'verbose': verbose,
    #         })
    # 
    # # Gather related objects
    # for rel in opts.get_all_related_objects() + opts.get_all_related_many_to_many_objects():
    #     verbose = _("related `%(app_label)s.%(object_name)s` objects") % {'app_label': rel.opts.app_label, 'object_name': rel.opts.object_name}
    #     accessor = rel.get_accessor_name()
    #     fields.append({
    #         'name'      : "%s.all" % accessor,
    #         'data_type' : 'List',
    #         'verbose'   : utils.parse_rst(_("all %s") % verbose , 'model', _('model:') + opts.module_name),
    #     })
    #     fields.append({
    #         'name'      : "%s.count" % accessor,
    #         'data_type' : 'Integer',
    #         'verbose'   : utils.parse_rst(_("number of %s") % verbose , 'model', _('model:') + opts.module_name),
    #     })
    # return render_to_response('simpleadmindoc/model_detail.html', {
    #     'root_path': get_root_path(),
    #     'name': '%s.%s' % (opts.app_label, opts.object_name),
    #     'summary': _("Fields on %s objects") % opts.object_name,
    #     'description': model.__doc__,
    #     'fields': fields,
    # }, context_instance=RequestContext(request))
model_detail = staff_member_required(model_detail)