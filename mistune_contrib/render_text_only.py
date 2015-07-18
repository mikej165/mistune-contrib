from mistune import Renderer


class TextRenderer(Renderer):
    """
    A text-only renderer. Useful from stripping markdown from a document
    """
    def block_code(self, code, lang=None):
        return code

    def block_quote(self, text):
        return text

    def block_html(self, html):
        return '\n'

    def header(self, text, level, raw=None):
        return text

    def hrule(self):
        return '\n'

    def list(self, body, ordered=True):
        return body

    def list_item(self, text):
        return text

    def paragraph(self, text):
        return "%s\n" % text.strip(' ')

    def table(self, header, body):
        return '%s\n%s' % (header, body)

    def table_row(self, content):
        return content

    def table_cell(self, content, **flags):
        return " %s " % content

    def double_emphasis(self, text):
        return text

    def emphasis(self, text):
        return text

    def codespan(self, text):
        return text

    def linebreak(self):
        return '\n'

    def strikethrough(self, text):
        return text

    def text(self, text):
        return text

    def autolink(self, link, is_email=False):
        return ''

    def link(self, link, title, text):
        return text

    def image(self, src, title, text):
        return "%s %s" % (title, text)

    def inline_html(self, html):
        return ''

    def footnote_ref(self, key, index):
        return ''

    def footnote_item(self, key, text):
        return text

    def footnotes(self, text):
        return text
