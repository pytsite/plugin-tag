"""PytSite Tag Plugin
"""
# Public API
from ._api import dispense, find_by_alias, find_by_title, get
from . import _model as model, _field as field, _widget as widget

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
