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

html_show_sourcelink = False
html_logo = "../html-logo.jpg"