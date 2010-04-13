{% spaceless %}
.. |title| replace:: {{ app_label }}

{% block title %}|title|
======={% endblock title %}{% block description %}
{% endblock description %}{% block toc %}
.. toctree::
	:glob:

	*
{% endblock toc %}{% block notes %}
{% endblock notes %}
{% endspaceless %}