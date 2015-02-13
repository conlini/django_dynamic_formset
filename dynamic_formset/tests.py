from django.test import TestCase
from dynamic_formset import *

# Create your tests here.

class AnchorWidgetTest(TestCase):

    def test_anchor_widget_render(self):
        widget = AnchorWidget("The Link", "/path/to/go",
                              {'style': "width: 100%"})
        rendered = widget.render(None, None, widget.attrs)
        print rendered
        self.assertIn(
            "<a{&#39;style&#39;: &#39;width: 100%&#39;, "
            "&#39;href&#39;: &#39;/path/to/go&#39;}>The Link</a>",
            rendered, "")
