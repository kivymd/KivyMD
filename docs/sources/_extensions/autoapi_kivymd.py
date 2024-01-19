"""
Monkey patching for AutoAPI Sphinx module.

Arrange .rst files by their summaries. Write path in the first line of docstring
to add .rst file. For example, "Classes/My Cool Class" will be placed in
"/classes/my-cool-class/index.rst".

It patches :func:`autoapi.mappers.python.objects.PythonPythonMapper.include_dir`,
:func:`autoapi.mappers.python.objects.PythonPythonMapper.pathname`,
:func:`autoapi.mappers.python.mapper.PythonSphinxMapper.output_rst`.
"""

import os
import re

import autoapi
import sphinx
# import unidecode
from autoapi.directives import NestedParse
from autoapi.extension import LOGGER
from autoapi.extension import setup as autoapi_setup
from autoapi.mappers.python.mapper import PythonSphinxMapper
from autoapi.mappers.python.objects import PythonPythonMapper
from docutils import nodes
from sphinx.util.console import bold, darkgreen
from sphinx.util.nodes import nested_parse_with_titles
from sphinx.util.osutil import ensuredir


def PythonPythonMapper_include_dir(self: PythonPythonMapper, root):
    if os.path.isabs(root):
        parts = [str(self.app.confdir)]
    else:
        parts = [""]  # Config root folder
    parts.extend(self.pathname.split(os.path.sep))
    return "/".join(parts)


def PythonPythonMapper_pathname(self: PythonPythonMapper):
    try:
        slug = self.summary
    except AttributeError:
        return os.path.join(*self.name.split("."))
    # slug = unidecode.unidecode(slug)
    slug = slug.lower()
    slug = re.sub(r"[^\w\./]+", "-", slug).strip("-")
    slug_split = slug.split("/")
    if slug == "" or len(slug_split) == 1 or self.type == "package":
        return os.path.join("api", *self.name.split("."))
    return os.path.join(*slug_split)


def PythonSphinxMapper_output_rst(
    self: PythonSphinxMapper, root, source_suffix
):
    for _, obj in sphinx.util.display.status_iterator(
        self.objects.items(),
        bold("[AutoAPI] ") + "Rendering Data... ",
        length=len(self.objects),
        verbosity=1,
        stringify_func=(lambda x: x[0]),
    ):
        rst = obj.render(
            include_summaries=self.app.config.autoapi_include_summaries
        )
        if not rst:
            continue

        detail_dir = obj.include_dir(root=root)
        ensuredir(detail_dir)
        path = os.path.join(detail_dir, "%s%s" % ("index", source_suffix))
        open(path, "wt", encoding="utf-8").write(rst)

        if not hasattr(self.app, "created_api_files"):
            self.app.created_api_files = []
        self.app.created_api_files.append(path)

        if not obj.pathname.startswith("api"):
            path_in_rst = f"/{obj.pathname.replace(os.sep, '/')}/index"
            index_dir = os.path.dirname(detail_dir)
            index_file = os.path.join(index_dir, "index" + source_suffix)
            if not os.path.exists(index_file):
                try:
                    index_name = obj.summary.split("/")[-2]
                except IndexError:
                    continue
                index_rst = (
                    f"{index_name}\n"
                    f"{'=' * len(index_name)}\n\n"
                    f".. toctree::\n"
                    f"    :maxdepth: 1\n"
                    f"    :sorted:\n\n"
                )
                if index_file not in self.app.created_api_files:
                    self.app.created_api_files.append(index_file)
            else:
                index_file_contents = open(
                    index_file, "rt", encoding="utf-8"
                ).read()
                if path_in_rst in index_file_contents:
                    continue
                index_rst = ""
            index_rst += f"    {path_in_rst}\n"
            ensuredir(index_dir)
            open(index_file, "at+", encoding="utf-8").write(index_rst)

    if self.app.config.autoapi_add_toctree_entry:
        self._output_top_rst(root)


def extension_build_finished(app, exception):
    if (
        not app.config.autoapi_keep_files
        and app.config.autoapi_generate_api_docs
    ):
        if app.verbosity > 1:
            LOGGER.info(
                bold("[AutoAPI] ") + darkgreen("Cleaning generated .rst files")
            )
        to_remove = getattr(app, "created_api_files", [])
        for file in to_remove:
            os.remove(file)
            directory = os.path.dirname(file)
            while True:
                try:
                    if len(os.listdir(directory)) > 0:
                        break
                    os.rmdir(directory)
                    directory = os.path.dirname(directory)
                except PermissionError:
                    break


def patched_nested_parse_run(self):
    node = nodes.container()
    node.document = self.state.document
    nested_parse_with_titles(self.state, self.content, node)
    try:
        title_node = node[0][0]
        if isinstance(title_node, nodes.title):
            title_node.children.pop(0)
    except IndexError:
        pass
    return node.children


def setup(app):
    NestedParse.run = patched_nested_parse_run
    PythonPythonMapper.pathname = property(PythonPythonMapper_pathname)
    PythonPythonMapper.include_dir = PythonPythonMapper_include_dir
    PythonSphinxMapper.output_rst = PythonSphinxMapper_output_rst
    autoapi.extension.build_finished = extension_build_finished
    autoapi_setup(app)
