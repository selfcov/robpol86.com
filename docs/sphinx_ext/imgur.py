"""Custom Sphinx "roles" for inline Imgur images and embedded albums."""

import re

from docutils import nodes

RE_IMGUR_ID = re.compile(r'^[a-zA-Z0-9]{5,10}')


def setup(app):
    """Called by Sphinx during phase 0 (initialization).

    :param app: Sphinx application object.
    """
    app.add_role('imgur', imgur_role)
    app.add_role('imgur_album', imgur_role)


def imgur_role(name, rawtext, text, *_):
    """Docutils role for an Imgur image or album.

    Called by Sphinx during phase 1 (reading). Represents a single docutils role in a document.
    """
    album = bool(name == 'imgur_album')
    imgur_id = RE_IMGUR_ID.findall(text)[0]
    #client = ImgurClient(os.environ['IMGUR_ID'], os.environ['IMGUR_SECRET'])
    #response = client.get_album(imgur_id) if album else client.get_image(imgur_id)

    if album:
        url = 'http://imgur.com/{}'.format(imgur_id)
        a_href = nodes.reference(rawtext, text, refuri=url)
        return [a_href], []

    url = 'http://imgur.com/{}'.format(imgur_id)
    a_href = nodes.reference(rawtext, text, refuri=url)
    return [a_href], []
