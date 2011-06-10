===========================
django-simpleadmindoc 0.4.0
===========================

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

Usage
-----

::

  .. djangoadmin:model:: books.Article

  Reference models :djangoadmin:model:`books.Article` or attributes
  :djangoadmin:attribute:`books.Article.headline`.

``djangoadmin:model`` directive in first line will autodocument all available
fields in ``Article`` model that is in ``books`` app.

References in second line will be replaced with verbose names and linked
to respective model / attribute.

Configuration
-------------

1. Add djangoadmin domain to sphinx coniguration (``conf.py``)::

    extensions = ["simpleadmindoc.ext.djangoadmindoc"]

2. Configure sphinx so it have have access to django website.
   Add website directory to ``sys.path`` and setup environment variable 
   ``DJANGO_SETTINGS_MODULE``::

        import sys, os
        sys.path.insert(0, os.path.abspath('../..'))
        sys.path.insert(0, os.path.abspath('..'))
        os.environ['DJANGO_SETTINGS_MODULE'] = 'example.settings'

3. Add `simpleadmindoc` to your settings `INSTALLED_APPS`.


Example application
-------------------

Small example application is included.

Requirements
------------

* Sphinx 1.0.1

Documentation
-------------

http://readthedocs.org/docs/simpleadmindoc/en/latest/

Contribute
----------

Fork + pull.
