{% spaceless %}
|project_name|
==============
{% block description %}{% endblock description %}

{% block toc %}
.. toctree::
	:glob:
	:maxdepth: 2

	apps/*/app
	*
{% endblock toc %}
{% block notes %}{% endblock notes %}
{% endspaceless %}
