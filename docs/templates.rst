Templates
=========

Index document
^^^^^^^^^^^^^^

Index document render following template: ::

  templates = ('simpleadmindoc/index.rst', )
  
Default implementation is:

.. code-block:: django

  {% spaceless %}
  |project_name|
  ==============
  {% block description %}{% endblock description %}

  {% block toc %}
  .. toctree::
    :glob:
    :maxdepth: 3

    apps/index
  {% endblock toc %}
  {% block notes %}{% endblock notes %}
  {% endspaceless %}

Application documents
^^^^^^^^^^^^^^^^^^^^^

Application documentation select template from: ::

  templates = ('simpleadmindoc/%s/app.rst' % app_label, 
              'simpleadmindoc/app.rst')

Default implementation is:

.. code-block:: django

  {% spaceless %}
  .. |title| replace:: {{ app_label }}

  {% block title %}|title|
  ======={% endblock title %}
  .. djangoadmin:app:: {{ app_label }} {{ app_label }}
  {% block description %}
  {% endblock description %}{% block toc %}
  .. toctree::
    :glob:

    *
  {% endblock toc %}{% block notes %}
  {% endblock notes %}
  {% endspaceless %}

Model documents
^^^^^^^^^^^^^^^^

Index document render following template: ::

  templates = ('simpleadmindoc/%s/%s.rst' % (model._meta.app_label, model.__name__.lower()), 
              'simpleadmindoc/%s/model.rst' % model._meta.app_label, 
              'simpleadmindoc/model.rst')

Default implementation is:

.. code-block:: django

  {% spaceless %}
  {% load simpleadmindoc_tags %}
  {% load i18n %}
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
