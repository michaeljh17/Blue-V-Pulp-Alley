class CellBuilder(object):
    """description of class"""

    def build_cell(self, input_text, length, border_char):
        print(input_text)
        # return string that is of X length with the input ending with border input
        string = '{:<' + str(length) + '}'
        string = string.format(input_text) + border_char
        return string

