"""PytSite Tag Plugin Widgets
"""
from plugins import odm as _odm, taxonomy as _taxonomy

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class TagCloud(_taxonomy.widget.Cloud):
    """Tag Cloud.
    """

    def __init__(self, uid: str, **kwargs):
        """Init.
        """
        super().__init__(uid, model='tag', **kwargs)


class EntityTagCloud(_taxonomy.widget.Cloud):
    """Tag Cloud of the Entity.
    """

    def __init__(self, uid: str, **kwargs):
        """Init.
        """
        super().__init__(uid, model='tag', **kwargs)

        self._entity = kwargs.get('entity')  # type: _odm.model.Entity

        if not self._entity:
            raise ValueError('Entity is not specified.')

        if not isinstance(self._entity, _odm.model.Entity):
            raise RuntimeError('{} is not an ODM entity instance'.format(type(self._entity)))

        if not self._entity.has_field('tags'):
            raise RuntimeError("Entity does not have 'tags' field")

    @property
    def terms(self) -> tuple:
        return self._entity.f_get('tags')
