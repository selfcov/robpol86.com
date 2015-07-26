import time

import sphinx_rtd_theme


# General configuration.
author = 'Robpol86'
copyright = '{}, Robpol86'.format(time.strftime('%Y'))
master_doc = 'index'
project = 'Robpol86.com'
release = '1.0'
version = release


# Options for HTML output.
html_favicon = 'favicon.ico'
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_title = project
