django-simpleadmindoc
=====================

`simpleadmindoc` is a django application that allows quickly creating documentation for django admin application in many formats such as HTML, PDF, etc. It is based on and produces documents for Sphinx.

Goal of `simpleadmindoc` is to make writing of documentation for editors and administrators fast, flexible and easy.

Example application
-------------------

Small example application and sample documentation for it is included. It is in `example` folder, and build HTML documentation is in  `example/simpleadmindoc/_build`.

![simpleadmindoc screenshot](http://github.com/bmihelac/django-simpleadmindoc/raw/master/example/simpleadmindoc.jpg)

Requirements
------------

* Sphinx 1.0

In the time of writing, *Sphinx 1.0* is not released yet, it can be downloaded from http://bitbucket.org/birkenfeld/sphinx/

Getting started
---------------

1. Add `simpleadmindoc` to your settings `INSTALLED_APPS`.
	
2. Create `simpleadmindoc` folder and and put Sphinx configuration file in it. Here is sample `config.py` file:

		# -*- coding: utf-8 -*-
		master_doc = 'index'

		project = u'ExampleApp'
		copyright = u'2010, example team'
		version = '1'
		release = '1.0'

		#language = None
		html_theme = 'sphinxdoc'

		extensions = ["simpleadmindoc.ext.djangoadmindoc"]

		rst_epilog = """
		.. |project_name| replace:: Example application admin documentation
		"""

		#html_show_sourcelink = False
		#html_logo = "html-logo.jpg"

3. Create documents

		./manage.py docgenapp APP1
	
	This will create documentation skeleton for application APP1 in `simpleadmindoc` folder:
	
	index.rst
	apps/APP1/app.rst
	apps/APP1/MODELNAME.rst

4. Build documentation

	Go to `simpleadmindoc` folder and run:
	
		sphinx-build -b html project_path/simpleadmindoc project_path/media/simpleadmindoc/

Write documentation
-------------------

Generated Sphinx documents can be (of course) edited directly but because `simpleadmindoc` uses standard Django templates to produce documentation skeleton, it should be easier to override this templates for application and model.
