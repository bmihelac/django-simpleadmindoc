django-simpleadmindoc
===========================

Simpleadmindoc is django application that allows you to quickly create help for modules in Django admin. 
Goal is to be flexible enough, fast to create and easy to integrate. 

Getting started
===============

1. Add simpleadmindoc to your project.
2. Add to urlpatterns, before admin part:   
		`(r'^admin/help/', include('simpleadmindoc.urls')),`

All models are visible by default and for each model fields and many2many fields are displayed.
If you want to customize help screen for any model create template in templates/simpleadmindoc:  
`APP_NAME/modelname.html`

Example application
===============

Minimal example application is included. Go to `example` folder and run

	./manage.py runserver

Go to django admin and you will see Help in top right corner. 
Username and password are 'test'.

![simpleadmindoc screenshot](http://github.com/bmihelac/django-simpleadmindoc/raw/master/example/simpleadmindoc.jpg)

TODO
====

* make possible to add static content
* display only content for modules that editor have right to view
* jump to current module in help
