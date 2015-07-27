"""Custom Sphinx roles and nodes for inline Imgur images and embedded albums."""

import re

from docutils import nodes

RE_IMGUR_ID = re.compile(r'^[a-zA-Z0-9]{5,10}')


class ImgurBlockQuote(nodes.Element):
    """Imgur embedded album <blockquote /> node."""

    @staticmethod
    def visit(spht, node):
        imgur_id = node.attributes.pop('imgur_id')
        html_attributes_bq = {'CLASS': 'imgur-embed-pub', 'lang': 'en', 'data-id': 'a/{}'.format(imgur_id)}
        spht.body.append(spht.starttag(node, 'blockquote', '', **html_attributes_bq))
        html_attributes_ah = dict(href='https://imgur.com/a/{}'.format(imgur_id), CLASS='reference external')
        spht.body.append(spht.starttag(node, 'a', 'Loading...', **html_attributes_ah))

    @staticmethod
    def depart(spht, _):
        spht.body.append('</a>')
        spht.body.append('</blockquote>')


def imgur_role(name, rawtext, text, *_):
    """Docutils role for an Imgur image or album.

    Called by Sphinx during phase 1 (reading). Represents a single docutils role in a document.
    """
    album = bool(name == 'imgur_album')
    imgur_id = RE_IMGUR_ID.findall(text)[0]
    #client = ImgurClient(os.environ['IMGUR_ID'], os.environ['IMGUR_SECRET'])
    #response = client.get_album(imgur_id) if album else client.get_image(imgur_id)

    if album:
        node = ImgurBlockQuote(rawtext)
        node.attributes['imgur_id'] = imgur_id
        return [node], []

    url = 'http://imgur.com/{}'.format(imgur_id)
    a_href = nodes.reference(rawtext, text, refuri=url)
    return [a_href], []


def setup(app):
    """Called by Sphinx during phase 0 (initialization).

    :param app: Sphinx application object.
    """
    app.add_node(ImgurBlockQuote, html=(ImgurBlockQuote.visit, ImgurBlockQuote.depart))
    app.add_role('imgur', imgur_role)
    app.add_role('imgur_album', imgur_role)
