Sphinx domain djangoadmin
=========================

Django app
----------

.. code-block:: rest

  .. djangoadmin:app:: books Books application

Django modeladmin class
-----------------------

.. code-block:: rest

  .. djangoadmin:class:: books.Article Article

Django model attribute
----------------------

.. code-block:: rest

  .. djangoadmin:attribute:: books.Publication.title Publication title

Cross referencing
-----------------

.. code-block:: rest

	You can cross reference other model with :djangoadmin:class:`books.Article`.
	Or attributes in other models like :djangoadmin:attribute:`books.Article.headline`.
