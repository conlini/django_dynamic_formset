from django.forms.formsets import BaseFormSet, ManagementForm, \
    TOTAL_FORM_COUNT, INITIAL_FORM_COUNT, MAX_NUM_FORM_COUNT, \
    MIN_NUM_FORM_COUNT
from django.core.exceptions import ValidationError
from django.forms.models import BaseModelFormSet

from dynamic_formset import *


class DynamicManagementForm(ManagementForm):
    def __init__(self, *args, **kwargs):
        self.base_fields['ADD_FORM'] = AnchorField("Add")
        super(DynamicManagementForm, self).__init__(*args, **kwargs)


class DynamicFormSet(BaseFormSet):
    @property
    def management_form(self):
        """Returns the ManagementForm instance for this FormSet."""
        if self.is_bound:
            form = DynamicManagementForm(self.data, auto_id=self.auto_id,
                                         prefix=self.prefix)
            if not form.is_valid():
                raise ValidationError(
                    _(
                        'ManagementForm data is missing or has been tampered with'),
                    code='missing_management_form',
                )
        else:
            form = DynamicManagementForm(auto_id=self.auto_id,
                                         prefix=self.prefix,
                                         initial={
                                             TOTAL_FORM_COUNT: self.total_form_count(),
                                             INITIAL_FORM_COUNT: self.initial_form_count(),
                                             MIN_NUM_FORM_COUNT: self.min_num,
                                             MAX_NUM_FORM_COUNT: self.max_num
                                         })
        return form


class DynamicModelFormSet(BaseModelFormSet, DynamicFormSet):
    pass