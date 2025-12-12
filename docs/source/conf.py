# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MetPyIR'
copyright = '2025, Xandra Campo'
author = 'Xandra Campo'
release = '0.0.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "pydata_sphinx_theme",
    "sphinx_multiversion",
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_title = f'{project} {release}'
html_theme_options = {
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["navbar-icon-links"],
    "show_nav_level": 2,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/lmri-met/metpyir",
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        }
    ],
    "switcher": {
        "json_url": "_static/versions.json",
        "version_match": release,
    },
}

smv_tag_whitelist = r"^v\d+\.\d+\.\d+$"  # matches tags like v1.0.0
smv_branch_whitelist = r"^$"  # matches no branches
smv_remote_whitelist = r"^origin$"  # matches only the origin remote
smv_latest_version = "v0.0.2"  # replace with your latest version tag
