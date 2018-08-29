"""PytSite Tag Plugin API Functions
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from typing import Iterable as _Iterable, Optional as _Optional
from plugins import odm as _odm, taxonomy as _taxonomy
from . import _model


def get(limit: int = 0, language: str = None) -> _Iterable[_model.Tag]:
    """Get tags
    """
    return _taxonomy.find('tag', language).sort([('weight', _odm.I_DESC)]).get(limit)


def dispense(title: str, alias: str = None, language: str = None, parent: _model.Tag = None) -> _model.Tag:
    """Create a new tag
    """
    return _taxonomy.dispense('tag', title, alias, language, parent)  # type: _model.Tag


def find_by_title(title: str, language: str = None) -> _Optional[_model.Tag]:
    """Get tag by title.
    """
    return _taxonomy.get('tag', title, language)  # type: _Optional[_model.Tag]


def find_by_alias(alias: str, language: str = None) -> _Optional[_model.Tag]:
    """Get tag by alias.
    """
    return _taxonomy.get('tag', alias=alias, language=language)
