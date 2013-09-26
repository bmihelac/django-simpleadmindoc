{% load simpleadmindoc_tags %}
{% rst_model_title opts.app_label opts.object_name %}

.. djangoadmin:model:: {{opts.app_label}}.{{opts.object_name}}
   :noautodoc:

{% render_model_attributes opts.app_label opts.object_name %}
