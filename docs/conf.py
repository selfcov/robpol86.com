import sphinx_rtd_theme


# General configuration.
author = 'Robpol86'
copyright = '2015, Robpol86'
exclude_patterns = ['_build']
extensions = []
language = None
master_doc = 'index'
project = 'Robpol86.com'
pygments_style = 'sphinx'
release = '1.0'
source_suffix = '.rst'
templates_path = ['_templates']
todo_include_todos = False
version = '1.0'


# Options for HTML output.
html_static_path = ['_static']
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
htmlhelp_basename = 'Robpol86comdoc'


# Options for LaTeX output.
latex_documents = [(master_doc, 'Robpol86com.tex', 'Robpol86.com Documentation', 'Robpol86', 'manual')]
latex_elements = {}


# Options for manual page output.
man_pages = [(master_doc, 'robpol86com', 'Robpol86.com Documentation', [author], 1)]


# Options for Texinfo output.
texinfo_documents = [
    (master_doc, 'Robpol86com', 'Robpol86.com Documentation', author, 'Robpol86com', 'One line description of project.',
     'Miscellaneous'),
]
