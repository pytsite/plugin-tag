"""PytSite Tag Plugin ODM Fields
"""
from pytsite import odm as _odm

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class Tag(_odm.field.Ref):
    """Tag ODM Field
    """

    def __init__(self, name: str, **kwargs):
        """Init
        """
        kwargs['model'] = 'tag'

        super().__init__(name, **kwargs)


class Tags(_odm.field.RefsUniqueList):
    """Tags ODM Field
    """

    def __init__(self, name: str, **kwargs):
        """Init
        """
        kwargs['model'] = 'tag'

        super().__init__(name, **kwargs)
