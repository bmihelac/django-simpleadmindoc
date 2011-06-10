Installation and configuration
==============================

Requirements
------------

* Sphinx 1.0.1

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
