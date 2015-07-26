"""Custom Sphinx "roles" for inline Imgur images and embedded albums."""

from docutils import nodes


def setup(app):
    """Called by Sphinx on ____ TODO."""
    app.add_role('imgur', imgur_role)


def imgur_role(name, rawtext, text, lineno, inliner, options=None, content=None):
    """TODO"""
    options = options or {}
    content = content or []

    url = 'http://imgur.com/{}'.format(text)
    a_href = nodes.reference(rawtext, text, refuri=url, **options)
    return [a_href], []
