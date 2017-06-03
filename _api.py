"""PytSite Tag Plugin API Functions
"""
from typing import Iterable as _Iterable, Optional as _Optional
from pytsite import odm as _odm
from plugins import taxonomy as _taxonomy
from . import _model

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def get(limit: int = 0, language: str = None) -> _Iterable[_model.Tag]:
    """Get tags.
    """
    return _taxonomy.find('tag', language).sort([('weight', _odm.I_DESC)]).get(limit)


def dispense(title: str, alias: str = None, language: str = None) -> _model.Tag:
    term = _taxonomy.dispense('tag', title, alias, language)  # type: _model.Tag

    return term


def find_by_title(title: str, language: str = None) -> _Optional[_model.Tag]:
    """Get tag by title.
    """
    return _taxonomy.find_by_title('tag', title, language)  # type: _Optional[_model.Tag]


def find_by_alias(alias: str, language: str = None) -> _Optional[_model.Tag]:
    """Get tag by alias.
    """
    return _taxonomy.find_by_alias('tag', alias, language)
