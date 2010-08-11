How it works
============

**django-simpleadmindoc** defines `Sphinx domain <http://sphinx.pocoo.org/domains.html>`_ for django admin.
This allows cross referencing apps, models and attributes in documentation. 
More information about djangoadmin domain in :doc:`here <djangoadmin_domain>`.

**django-simpleadmindoc** `docgenapp` management command create skeleton for documentation. 
It would create skeleton for following documents:

* `index` document
* for every application `app` document in `apps` directory
* for every model in application `modelname` document in `apps` directory

`docgenapp` uses standard django templates to generate skeleton documents. 
This allows developer to extend and change django templates to suits their needs, per model, project or application.
More documentation about available templates is available :doc:`here <templates>`.

`docgenapp` also process documents found in `simpleadmindoc_static` template directories and save 
them to `doc` folder, keeping the directory structure. It would look for documents both in `TEMPLATE_DIRS` and 
individual `app_directories` directories.

Skeleton documentation are ready to be processed by Sphinx:

.. code-block:: bash

  $ sphinx-build -b html docs /path_where_to_put_html_dcumentation/
