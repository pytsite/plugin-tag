"""PytSite Tag Plugin
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

# Public API
from ._api import get, dispense, find_by_alias, find_by_title
from . import _model as model, _field as field, _widget as widget


def plugin_load():
    from pytsite import lang
    from plugins import taxonomy
    from . import _model

    lang.register_package(__name__)
    taxonomy.register_model('tag', _model.Tag, 'tag@tags', menu_roles='dev')
