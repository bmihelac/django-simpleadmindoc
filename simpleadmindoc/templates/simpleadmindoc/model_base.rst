{% spaceless %}
{% load simpleadmindoc_tags %}
.. |title| replace:: {{  opts.verbose_name_plural }}

{% block title %}|title|
======={% endblock title %}
.. djangoadmin:class:: {{opts.app_label}}.{{opts.object_name}} {{opts.verbose_name}}
{% block description %}{% endblock description %}{% block model_fields %}
Fields
------
{% fields_for_model opts %}{% endblock model_fields %}{% block notes %}
{% endblock notes %}
{% endspaceless %}
