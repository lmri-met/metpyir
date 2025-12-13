# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'MetPyIR'
copyright = '2025, Xandra Campo'
author = 'Xandra Campo'
release = 'v0.0.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "pydata_sphinx_theme",
    "sphinx_multiversion",
]

templates_path = ['_templates']
exclude_patterns = []

# --- sphinx-multiversion configuration ---

# SmvSelectBranchWhenChanged determines if the current branch/tag is selected when the page changes.
# If True, it tries to keep the user on the same version when they switch pages.
# If False, the version will always reset to the default.
smv_select_branch_when_changed = True

# SmvTagPatterns: Only include versions that match this pattern (e.g., tags starting with 'v')
# Use '[\d\.]+' to match versions like '1.0', '1.2.3', etc.
smv_tag_patterns = r'^v\d+\.\d+(\.\d+)?$'

# SmvBranchPatterns: Only include branches that match this pattern
smv_branch_patterns = r'^(main|master)$'

# SmvLatestVersion: Set the branch/tag to be considered the 'latest' or 'stable' version.
smv_latest_version = 'main'  # or 'master' or a specific tag like 'v2.0.0'

# SmvOldestVersion: Set the oldest version to display in the dropdown.
smv_oldest_version = None  # Set to a specific version string if needed, e.g., 'v1.0.0'

# SmvRootRef: The branch/tag to use as the base for building. Usually 'main' or 'master'.
# Files like conf.py are read from this reference.
smv_root_ref = 'main'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_title = f'{project}'
html_theme_options = {
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["version-switcher", "navbar-icon-links"],
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
html_baseurl = '/metpyir/'
