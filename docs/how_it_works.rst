How it works
============

django-simpleadmindoc defines `Sphinx domain <http://sphinx.pocoo.org/domains.html>`_ for django admin.
This allows cross referencing apps, models and attributes in documentation. 
More information about djangoadmin domain in :doc:`djangoadmin_domain`.

django-simpleadmindoc create skeleton for documentation. It would create skeleton for following documents:

* `index` document
* for every application `app` document
* for every model in application `modelname` document

django-simpleadmindoc uses standard django templates to generate skeleton documents. 
This allows developer to extend and change django templates to suits their needs, per model, project or application.
More documentation about available templates is available :doc:`here <templates>`.

django-simpleadmindoc process static documents and save them to `doc` folder.
This allows developer to embed default documentation for given app.

Skeleton documentation are to be processed by 
