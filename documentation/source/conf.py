# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import pdb
import sys
import os
sys.path.insert(0, os.path.abspath('../../'))
sys.path.insert(0, os.path.abspath('./'))

# -- Project information -----------------------------------------------------

project = 'do-mpc'
copyright = '2021, Sergio Lucia and Felix Fiedler'
author = 'Sergio Lucia and Felix Fiedler'

# The full version, including alpha/beta/rc tags
exec(open('../../do_mpc/_version.py').read())

release = __version__



# -- General configuration ---------------------------------------------------

# The master toctree document.
master_doc = 'index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx_rtd_theme',
	      'sphinx.ext.intersphinx',
          'nbsphinx',
          'sphinx.ext.mathjax',
          'sphinx.ext.graphviz',
          'sphinx.ext.autosummary',
          'sphinx.ext.viewcode',
          'sphinx_copybutton',
          'myst_parser',
              ]

graphviz_output_format = 'svg'

autosummary_generate = True

mathjax3_config = {
    'extensions': ['tex2jax.js'],
    'jax': ['input/TeX', 'output/HTML-CSS'],
}

# Order methods in documentation by their appearence in the sourcecode:
autodoc_member_order = 'bysource'
# Delete this previous line, to autoclass_content = "both"  # Add __init__ doc (ie. params) to class summaries
autodoc_inherit_docstrings = True  # If no docstring, inherit from base class
nbsphinx_allow_errors = True  # Continue through Jupyter errors
add_module_names = False # Remove namespaces from class/method signaturesorder by alphabet.
autosummary_imported_members = True # https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html#confval-autosummary_ignore_module_all 
autosummary_ignore_module_all = False
autodoc_mock_imports = ["casadi", "casadi.tools"] # With autosummary_imported_members = True, this avoids documenting packages that are imported with from ... import *.

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', '**.ipynb_checkpoints']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'logo_only': True,
    'navigation_depth': 4,
}
html_theme_path = ["../.."]
html_logo = "static/dompc_var_02_white.svg"
html_show_sourcelink = True

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['static']


# -- Options for LaTeX output ---------------------------------------------
latex_engine ='pdflatex'


# -- Run custom script -----------------------------------------------------
import release_overview

# Get Markdown page with the overview over all releases from Github API.
release_overview.get_overview()
