{% spaceless %}
.. |title| replace:: All apps

{% block title %}|title|
======={% endblock title %}{% block description %}
{% endblock description %}{% block toc %}
.. toctree::
	:glob:
	:maxdepth: 2

	*/app
{% endblock toc %}{% block notes %}
{% endblock notes %}
{% endspaceless %}