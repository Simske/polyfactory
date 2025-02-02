from __future__ import annotations

from functools import partial
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from sphinx.addnodes import document
    from sphinx.application import Sphinx


project = "Polyfactory"
copyright = "2023, Litestar Org"
author = "Litestar Org"
release = "1.0.0"

extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_design",
    "auto_pytabs.sphinx_ext",
    "sphinx_copybutton",
    "sphinxcontrib.mermaid",
]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "faker": ("https://faker.readthedocs.io/en/master/", None),
    "pytest": ("https://docs.pytest.org/en/latest/", None),
}

napoleon_google_docstring = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = False
napoleon_attr_annotations = True

autoclass_content = "class"
autodoc_class_signature = "separated"
autodoc_default_options = {"special-members": "__init__", "show-inheritance": True, "members": True}
autodoc_member_order = "bysource"
autodoc_typehints_format = "short"

auto_pytabs_min_version = (3, 8)
auto_pytabs_max_version = (3, 11)
auto_pytabs_compat_mode = True

autosectionlabel_prefix_document = True

suppress_warnings = [
    "autosectionlabel.*",
    "ref.python",  # TODO: remove when https://github.com/sphinx-doc/sphinx/issues/4961 is fixed
]

html_theme = "litestar_sphinx_theme"
html_static_path = ["_static"]
html_show_sourcelink = False
html_title = "Polyfactory"

nitpicky = True
nitpick_ignore = [
    ("py:class", "BaseModel"),
    ("py:class", "Decimal"),
    ("py:class", "Faker"),
    ("py:class", "FieldInfo"),
    ("py:class", "Random"),
    ("py:class", "Scope"),
    ("py:class", "T"),
    ("py:class", "P"),
    ("py:class", "P.args"),
    ("py:class", "P.kwargs"),
    ("py:class", "Self"),
    ("py:class", "TypeGuard"),
    ("py:class", "date"),
]
nitpick_ignore_regex = [
    (r"py:.*", r"typing_extensions.*"),
    (r"py:.*", r"polyfactory.*\.T"),
    (r"py:.*", r"polyfactory.*\.P"),
    (r"py:.*", r".*TypedDictT"),
    (r"py:.*", r"pydantic.*"),
    (r"py:.*", r"msgspec.*"),
]

html_theme_options = {
    "use_page_nav": False,
    "github_repo_name": "polyfactory",
    "logo": {
        "link": "https://polyfactory.litestar.dev",
    },
    "extra_navbar_items": {
        "Documentation": "index",
        "Community": {
            "Contributing": {
                "description": "Learn how to contribute to Polyfactory",
                "link": "contributing",
                "icon": "contributing",
            },
            "Code of Conduct": {
                "description": "Review the etiquette for interacting with the Litestar community",
                "link": "https://github.com/litestar-org/.github/blob/main/CODE_OF_CONDUCT.md",
                "icon": "coc",
            },
        },
        "About": {
            "Litestar Organization": {
                "description": "About the Litestar organization",
                "link": "https://litestar.dev/about/organization.html",
                "icon": "org",
            },
        },
    },
}


def update_html_context(
    app: Sphinx, pagename: str, templatename: str, context: dict[str, Any], doctree: document
) -> None:
    context["generate_toctree_html"] = partial(context["generate_toctree_html"], startdepth=0)


def setup(app: Sphinx) -> dict[str, bool]:
    app.setup_extension("litestar_sphinx_theme")
    app.setup_extension("pydata_sphinx_theme")
    app.connect("html-page-context", update_html_context)

    return {"parallel_read_safe": True, "parallel_write_safe": True}
