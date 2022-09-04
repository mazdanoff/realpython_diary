from web_elements.element import Element


class InputField(Element):

    @property
    def value(self):
        return self.element.get_attribute('value')

    @value.setter
    def value(self, v):
        self.element.clear()
        self.element.send_keys(v)
