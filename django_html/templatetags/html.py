"""
{% doctype "html4" %}
{% doctype "html4" silent %} <!-- set internal doctype, NOT output it -->
{% doctype "html4trans" %}
{% doctype "html5" %}
{% doctype "xhtml1" %}
{% doctype "xhtml1trans" %}
"""

doctypes = {
  'html4': """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
    "http://www.w3.org/TR/html4/strict.dtd">""",
  'html4trans': """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
    "http://www.w3.org/TR/html4/loose.dtd">""",
  'xhtml1': """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">""",
  'xhtml1trans': """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">""",
  'html5': '<!DOCTYPE html>',
}
html_doctypes = ('html4', 'html5', 'html4trans')

from django import template
register = template.Library()

def do_doctype(parser, token):
    bits = token.split_contents()
    if len(bits) not in (2, 3):
        raise template.TemplateSyntaxError, \
            "%r tag requires 1-2 arguments" % bits[0]
    if len(bits) == 3 and bits[2] != 'silent':
        raise template.TemplateSyntaxError, \
            "If provided, %r tag second argument must be 'silent'" % bits[0]
    # If doctype is wrapped in quotes, they should balance
    doctype = bits[1]
    if doctype[0] in ('"', "'") and doctype[-1] != doctype[0]:
        raise template.TemplateSyntaxError, \
            "%r tag quotes need to balance" % bits[0]
    return DoctypeNode(bits[1], is_silent = (len(bits) == 3))

class DoctypeNode(template.Node):
    def __init__(self, doctype, is_silent=False):
        self.doctype = doctype
        self.is_silent = is_silent
    
    def render(self, context):
        if self.doctype[0] in ('"', "'"):
            doctype = self.doctype[1:-1]
        else:
            try:
                doctype = template.resolve_variable(self.doctype, context)
            except template.VariableDoesNotExist:
                # Cheeky! Assume that they typed a doctype without quotes
                doctype = self.doctype
        # Set doctype in the context
        context._doctype = doctype
        if self.is_silent:
            return ''
        else:
            return doctypes.get(doctype, '')

register.tag('doctype', do_doctype)
