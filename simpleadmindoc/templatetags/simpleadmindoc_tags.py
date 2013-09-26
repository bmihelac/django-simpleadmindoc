from django import template

from simpleadmindoc.util import model_attributes


register = template.Library()


@register.simple_tag
def rst_title(title, level="="):
    content = [unicode(title),
            level * len(title)]
    return "\n".join(content)


@register.simple_tag
def rst_model_title(app_label, object_name, level="="):
    """
    RST verbose model title.
    """
    title = ":djangoadmin:model:`%s.%s`" % (
        app_label,
        object_name
    )
    return rst_title(title, level)


@register.simple_tag
def render_model_attributes(app_label, model_name):
    lst = []
    for name, opts in model_attributes(app_label, model_name).items():
        lst.append("  .. djangoadmin:attribute:: %s.%s.%s" % (app_label, model_name, name))
        lst.append('  ')
        description = unicode(opts['description'])
        if description:
            lst.append("     %s" % description)
            lst.append('  ')
    return '\n'.join(lst)
