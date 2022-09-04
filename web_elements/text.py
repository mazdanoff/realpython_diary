from web_elements.element import Element


class Text(Element):

    @property
    def value(self):
        return self.element.text
