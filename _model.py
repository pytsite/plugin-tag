"""PytSite Tag Plugin ODM Models
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from pytsite import events as _events
from plugins import odm as _odm, taxonomy as _taxonomy, odm_ui as _odm_ui, form as _form


class Tag(_taxonomy.model.Term):
    """Tag Model.
    """
    def _setup_fields(self):
        super()._setup_fields()
        self.remove_field('order')

    def _pre_delete(self, **kwargs):
        super()._pre_delete(**kwargs)

        _events.fire('tag@pre_delete', tag=self)

    @classmethod
    def odm_ui_browser_setup(cls, browser: _odm_ui.Browser):
        """Hook.
        """
        super().odm_ui_browser_setup(browser)

        browser.default_sort_field = 'weight'
        browser.default_sort_order = _odm.I_DESC

    def odm_ui_m_form_setup_widgets(self, frm: _form.Form):
        super().odm_ui_m_form_setup_widgets(frm)

        frm.remove_widget('_parent')
