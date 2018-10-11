"""PytSite Tag Plugin
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

# Public API
from ._api import get, dispense, find_by_alias, find_by_title
from . import _model as model, _field as field, _widget as widget
from ._model import Tag


def plugin_load():
    from plugins import taxonomy
    from . import _model

    taxonomy.register_model('tag', _model.Tag, 'tag@tags', menu_roles='dev')
