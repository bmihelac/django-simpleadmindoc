First steps with simpleadmindoc
===============================

1. Create sphinx documents (replace APP1 with your app):

  ./manage.py docgenapp APP1

This will create documentation skeleton in `docs` folder: ::

  index.rst
  apps/APP1/app.rst
  apps/APP1/MODELNAME.rst
  
To see which documents would be created see :doc:`how_it_works`.

2. Build documentation

Compile documentation into HTML: ::

  $ sphinx-build -b html docs /path_where_to_put_html_dcumentation/