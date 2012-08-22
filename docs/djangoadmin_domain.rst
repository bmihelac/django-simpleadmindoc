==================
djangoadmin domain
==================

Signatures are always in form::

    applabel_ModelName_attribute

Roles
-----

Verbose name of model or model attribute is used as text for link,
unless explicit title is specified.

Model role
^^^^^^^^^^

.. code-block:: rest

    You can cross reference other model with :djangoadmin:model:`books.Article`.

Model attribute role
^^^^^^^^^^^^^^^^^^^^

.. code-block:: rest

    Attributes in other models like :djangoadmin:attribute:`books.Article.headline`.

Unicode role
^^^^^^^^^^^^

.. code-block:: rest

    Translation using Django I18n machinery, :djangoadmin:unicode:`yes`.

Directives
----------

Model
^^^^^

.. code-block:: rest

  .. djangoadmin:model:: books.Article

     Description of Article model.

All model fields would be added automatically.

Options

* Normally, all model attributes will be documented. If you wish to exclude
  some attributes, use ``exclude`` option::

.. code-block:: rest

  .. djangoadmin:model:: books.Article
     :exclude: id, title

* Turn off autodocumenting with ``noautodoc`` flag.

.. code-block:: rest

  .. djangoadmin:model:: books.Article
     :noautodoc:

     .. djangoadmin:attribute:: books.Article.creation_date

        Creation date.

Model attribute
^^^^^^^^^^^^^^^

.. code-block:: rest

  .. djangoadmin:attribute:: books.Publication.title

Model attributes are automatically added when Model directive is called.

Current model
^^^^^^^^^^^^^

.. code-block:: rest

  .. djangoadmin:currentmodel:: books.Article

  Reference :djangoadmin:attribute:`headline`.

Sets current djangoadmin:model.
Allows using roles without app.model signature.


