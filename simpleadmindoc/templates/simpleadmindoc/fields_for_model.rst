{% load simpleadmindoc_tags %}
{% for field in fields %}
{% field_definition model_opts field %}
{% endfor %}
