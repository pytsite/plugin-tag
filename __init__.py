"""PytSite Tag Plugin.
"""
# Public API
from ._api import dispense_tag, find_tag_by_alias, find_tag_by_title, get_tags
from . import _model as model, _widget as widget

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def _init():
    from pytsite import lang
    from plugins import taxonomy
    from . import _model

    lang.register_package(__name__, alias='tag')
    taxonomy.register_model('tag', _model.Tag, 'tag@tags')


_init()
