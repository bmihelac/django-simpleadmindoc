{% spaceless %}
|project_name|
==============
{% block description %}{% endblock description %}

{% block toc %}
.. toctree::
	:glob:
	:maxdepth: 3

	apps/index
{% endblock toc %}
{% block notes %}{% endblock notes %}
{% endspaceless %}
