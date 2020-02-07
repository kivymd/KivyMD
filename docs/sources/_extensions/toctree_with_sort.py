from docutils.parsers.rst import directives
from sphinx.directives.other import TocTree, int_or_nothing


class TocTreeWithSort(TocTree):
    option_spec = {
        "maxdepth": int,
        "name": directives.unchanged,
        "caption": directives.unchanged_required,
        "glob": directives.flag,
        "hidden": directives.flag,
        "includehidden": directives.flag,
        "numbered": int_or_nothing,
        "titlesonly": directives.flag,
        "reversed": directives.flag,
        "sorted": directives.flag,
    }

    def parse_content(self, toctree):
        ret = super().parse_content(toctree)
        if "sorted" in self.options:
            toctree["entries"] = sorted(toctree["entries"])
        return ret


def setup(app):
    directives.register_directive("toctree", TocTreeWithSort)
