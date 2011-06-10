===================
Management commands
===================

docgenapp
---------

.. program:: docgenapp

Generate sphinx documentation skeleton for given apps.

Generated file structure::

    docs/APP_LABEL/index.rst
    docs/APP_LABEL/MODEL_NAME.rst
    docs/APP_LABEL/MODEL_NAME.rst

Options

.. option:: -l LOCALE, --locale=LOCALE

Activate given locale, verbose names for models and attributes will be
in given locale.

.. option:: --exclude-from=FILE

Exclude patterns for models that you do not want documentation to be
generated for.

.. option:: --path=PATH

Specify path where to save skeleton documentation.
All existing files would be overwritten.

