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

    @classmethod
    def on_register(cls, model: str):
        def section_pre_delete(section: _section.model.Section):
            tag = _taxonomy.find(model).inc('sections', section).first()  # type: Tag
            if tag:
                msg_args = {'section_title': section.title, 'tag_title': tag.f_get('title')}
                raise _errors.ForbidDeletion(_lang.t('tag@section_used_by_tag', msg_args))

        _events.listen('section.pre_delete', section_pre_delete)

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
