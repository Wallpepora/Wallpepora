# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Wallpepora'
copyright = '2025, Romain BOSSY'
author = 'Romain BOSSY'
release = '0.0.1'

needs_sphinx = "8.2.3"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "pydata_sphinx_theme"
htm_theme_options = {
    "navbar_align": "content", # Align the navigation bar with the content of the page
}
html_static_path = ['_static']

# Disable the "Show source" link
html_show_sourcelink = False

# Myst Parser config
myst_enable_extensions = [
    "colon_fence"
]