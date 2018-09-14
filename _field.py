"""PytSite Tag Plugin ODM Fields
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from plugins import odm as _odm


class Tags(_odm.field.RefsUniqueList):
    """Tags ODM Field
    """

    def __init__(self, name: str, **kwargs):
        """Init
        """
        kwargs['model'] = 'tag'

        super().__init__(name, **kwargs)
