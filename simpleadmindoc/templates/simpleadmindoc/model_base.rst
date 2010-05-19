{% spaceless %}
{% load simpleadmindoc_tags %}
{% load	i18n %}
.. |title| replace:: {{  opts.verbose_name_plural }}
.. |fields_title| replace:: {% trans "All fields" %}

{% block title %}|title|
======={% endblock title %}
.. djangoadmin:class:: {{opts.app_label}}.{{opts.object_name}} {{opts.verbose_name}}
{% block description %}{% endblock description %}{% block model_fields %}
|fields_title|
{% fields_for_model opts %}{% endblock model_fields %}{% block notes %}
{% endblock notes %}
{% endspaceless %}
