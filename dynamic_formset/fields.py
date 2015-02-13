from dynamic_formset import *
from django.forms.fields import Field


class AnchorField(Field):
    def __init__(self, title, href=None, *args, **kwargs):
        self.widget = AnchorWidget(title, href)
        super(AnchorField, self).__init__(required=False, widget=self.widget,
                                          label="", *args, **kwargs)