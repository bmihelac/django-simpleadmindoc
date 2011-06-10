django-simpleadmindoc
=====================

Django-simpleadmindoc is a tool that helps creating documentation for
editors and administrators of django based website.

Simpleadmindoc is based on and produces documents for 
`Sphinx <http://http://sphinx.pocoo.org/>`_.

Main features:

1. ``djangoadmin`` Sphinx domain allows autodocumenting models,

2. ``djangoadmin`` also allows referencing models and fields inside
   documentation while taking care of using verbose names,

3. ``docgenapp`` django management command allows fast creating of skeleton
   documentation for applications inside website.

Goal of simpleadmindoc is to make writing of documentation for editors and
administrators fast, flexible and easy.

.. toctree::
  :maxdepth: 2

  installation
  djangoadmin_domain
  management_commands
  todo
  changelog
