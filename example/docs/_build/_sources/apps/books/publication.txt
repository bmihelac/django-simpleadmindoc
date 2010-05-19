.. |title| replace:: Publications

|title|
=======
.. djangoadmin:class:: books.Publication Publication

Description of this model. Template for this document is in templates folder: `simpleadmindoc/books/publication.rst`.

You can cross reference other models like :djangoadmin:class:`books.Article`.

	.. code-block:: rest
	
		You can cross reference other models like :djangoadmin:class:`books.Article`.
		
Or attributes in other models like :djangoadmin:attribute:`books.Article.headline`.

	.. code-block:: rest

		Or attributes in other models like :djangoadmin:attribute:`books.Article.headline`.

		

Fields
------


.. djangoadmin:attribute:: books.Publication.id ID

	Integer

.. djangoadmin:attribute:: books.Publication.title Publication title

	String (up to 30)
