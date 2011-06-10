from django import template


register = template.Library()


@register.simple_tag
def rst_title(title, level="="):
    content = [title,
            level * len(title)]
    return "\n".join(content)
