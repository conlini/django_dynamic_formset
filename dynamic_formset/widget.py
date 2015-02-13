from django.forms.widgets import Widget
from django.utils.html import format_html
from django.forms.utils import flatatt


class AnchorWidget(Widget):
    def __init__(self, title, href=None, *args, **kwargs):
        super(AnchorWidget, self).__init__(*args, **kwargs)
        self.href = href
        self.title = title

    def render(self, name, value, attrs=None):
        final_attr = self.build_attrs(attrs)
        if self.href:
            final_attr['href'] = self.href

        return format_html("<a{0}>{1}</a>", flatatt(final_attr), self.title)
