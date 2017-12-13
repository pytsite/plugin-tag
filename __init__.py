"""PytSite Tag Plugin
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import plugman as _plugman

if _plugman.is_installed(__name__):
    # Public API
    from ._api import dispense, find_by_alias, find_by_title, get
    from . import _model as model, _field as field, _widget as widget


def plugin_load():
    from pytsite import lang
    from plugins import taxonomy
    from . import _model

    lang.register_package(__name__)
    taxonomy.register_model('tag', _model.Tag, 'tag@tags')
