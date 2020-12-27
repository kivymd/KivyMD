:github_url: https://github.com/kivymd/KivyMD/blob/master/{{ obj.obj.relative_path|replace("\\", "/") }}
{% if not obj.display %}
{# Do not display warnings #}
:orphan:
{% endif %}

{# Write last word in summary #}
{% set unincluded = obj.include_dir("").startswith("/api") %}
{% set summary_split = obj.summary.split("/") %}
{% set name = summary_split[-1] %}
{% if name %}
{{ name }}
{{ "=" * name|length }}
{% else %}
{{ obj.name }}
{{ "=" * obj.name|length }}
{% endif %}

.. py:module:: {{ obj.name }}

{# Write docstring of module #}
{% if obj.docstring %}
.. autoapi-nested-parse::

   {{ obj.docstring|prepare_docstring|indent(3) }}
{% endif %}

{% block api %}
{# API. Write module name #}
API - :mod:`{{ obj.name }}`
{{ "-" * 13 }}{{ "-" * obj.name|length }}

{% if obj.all is not none %}
{# Get all visible children #}
{% set visible_children = obj.children|selectattr("short_name", "in", obj.all)|list %}
{% elif obj.type is equalto("package") %}
{% set visible_children = obj.children|selectattr("display")|list %}
{% else %}
{% set visible_children = obj.children|selectattr("display")|rejectattr("imported")|list %}
{% endif %}
{% if visible_children %}
{# Write all visible children #}
{% for obj_item in visible_children %}
{{ obj_item.rendered|indent(0) }}
{% endfor %}
{% endif %}
{% endblock %}

{# Write submodules and subpackages if it is package #}
{% block submodules %}
{% set visible_submodules = obj.submodules|selectattr("display")|list %}
{% set visible_subpackages = obj.subpackages|selectattr("display")|list %}
{% if visible_submodules or visible_subpackages %}
Submodules
----------
{% if visible_submodules %}

.. toctree::
   :titlesonly:
   :maxdepth: 1

{% for submodule in visible_submodules %}
{% if unincluded == submodule.include_dir("").startswith("/api") %}
   {{ submodule.name }} <{{ submodule.include_dir("") }}/index>
{% endif %}
{% endfor %}
{% endif %}
{% if visible_subpackages %}

.. toctree::
   :titlesonly:
   :maxdepth: 3

{% for subpackage in visible_subpackages %}
{% if unincluded == subpackage.include_dir("").startswith("/api") %}
   {{ subpackage.name }} <{{ subpackage.include_dir("") }}/index>
{% endif %}
{% endfor %}
{% endif %}
{% endif %}
{% endblock %}
