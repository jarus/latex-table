# -*- coding: utf-8 -*-

from StringIO import StringIO

escape_mapping = {
    '&': '\\&',
    '%': '\\%',
    '$': '\\$',
    '#': '\\#',
    '_': '\\_',
    '{': '\\{',
    '}': '\\}',
    '~': '\\textasciitilde',
    '^': '\\textasciicircum',
    '\\': '\\textbackslash'
}


def escape(input_string):
    input_string = unicode(input_string)
    for value, escaped in escape_mapping.items():
        input_string.replace(value, escaped)
    return input_string


class LatexTable(object):

    row_strings = []

    def __init__(self, table_spec, position=None, centering=False,
                 caption=None):
        self.table_spec = table_spec
        self.position = position
        self.centering = centering
        self.caption = escape(caption)

    def add_row(self, *args):
        columns = []
        for column in args:
            columns.append(escape(unicode(column)))
        self.row_strings.append(u" & ".join(columns) + " \\\\")

    def add_hline(self):
        self.row_strings.append(u"\\hline")

    def to_latex(self):
        s = u""
        s += u"\\begin{table}"
        if self.position:
            s += u'[' + self.position + ']'
        s += u"\n"

        if self.centering:
            s += u"  \\centering\n"

        s += u'  \\begin{tabular}{' + self.table_spec + '}\n'
        for row in self.row_strings:
            s += "    " + row + u" \n"
        s += u'  \\end{tabular}\n'

        if self.caption:
            s += u'  \caption{' + self.caption + '}\n'

        s += u'\\end{table}\n'
        return s
