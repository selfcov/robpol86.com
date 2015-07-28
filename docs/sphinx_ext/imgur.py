"""Custom Sphinx roles and nodes for inline Imgur images and embedded albums."""

import re

from docutils import nodes
from docutils.parsers.rst import Directive

__author__ = '@Robpol86'
__license__ = 'MIT'
__version__ = '0.0.1'
RE_IMGUR_ID = re.compile(r'^[a-zA-Z0-9]{5,10}')


class ImgurBlockQuoteNode(nodes.General, nodes.Element):

    def __init__(self, imgur_id, is_album, hide_post_details):
        super().__init__()
        self.imgur_id = imgur_id
        self.is_album = is_album
        self.hide_post_details = hide_post_details


class ImgurBlockQuoteDirective(Directive):
    required_arguments = 1
    optional_arguments = 1
    option_spec = dict(hide_post_details=bool)

    def run(self):
        return [ImgurBlockQuoteNode(self.arguments[0], self.name == 'imgur-album', self.options['hide_post_details'])]


class EventHandlers(object):

    @classmethod
    def process_nodes(cls, app, doctree, fromdocname):
        for node in doctree.traverse(ImgurBlockQuoteNode):
            node.replace_self([nodes.Text('{} {} {}'.format(node.imgur_id, node.is_album, node.hide_post_details))])

    @classmethod
    def purge_from_cache(cls, app, env, docname):
        raise NotImplementedError


def setup(app):
    """Called by Sphinx during phase 0 (initialization).

    :param app: Sphinx application object.

    :returns: Extension version.
    :rtype: dict
    """
    # app.add_config_value('imgur_auth_id', None, False)
    # app.add_config_value('imgur_auth_secret', None, False)
    app.add_config_value('imgur_album_hide_post_details', False, True)
    # app.add_config_value('imgur_image_hide_post_details', False, True)
    app.add_node(ImgurBlockQuoteNode)
    # app.add_directive('imgur', ImgurBlockQuoteDirective)
    app.add_directive('imgur-album', ImgurBlockQuoteDirective)
    # app.add_role('imgur', imgur_role)
    # app.add_role('imgur-title', imgur_role)
    # app.add_role('imgur-description', imgur_role)
    app.connect('doctree-resolved', EventHandlers.process_nodes)
    # app.connect('env-purge-doc', EventHandlers.purge_from_cache)
    return dict(version=__version__)
