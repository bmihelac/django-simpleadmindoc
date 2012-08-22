{% load simpleadmindoc_tags %}
{% rst_title opts.verbose_name_plural %}

.. djangoadmin:model:: {{opts.app_label}}.{{opts.object_name}}
   :noautodoc:

{% render_model_attributes opts.app_label opts.object_name %}
