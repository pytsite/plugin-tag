"""PytSite Tag Plugin Models.
"""
from pytsite import odm as _odm, odm_ui as _odm_ui, events as _events, errors as _errors, lang as _lang
from plugins import taxonomy as _taxonomy, section as _section

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class Tag(_taxonomy.model.Term):
    """Tag Model.
    """

    def _setup_fields(self):
        """Hook.
        """
        super()._setup_fields()

        self.define_field(_odm.field.RefsUniqueList('sections', model='section'))

    @classmethod
    def odm_ui_browser_setup(cls, browser: _odm_ui.Browser):
        """Hook.
        """
        super().odm_ui_browser_setup(browser)

        browser.default_sort_field = 'weight'
        browser.default_sort_order = _odm.I_DESC

    def _pre_delete(self, **kwargs):
        super()._pre_delete(**kwargs)

        _events.fire('tag.pre_delete', tag=self)
