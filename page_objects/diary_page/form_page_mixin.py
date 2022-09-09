from web_elements.button import Button
from web_elements.input_field import InputField
from .form_page_mixin_locators import FormPageMixinLocators as Locators


class FormPageMixin:

    title = InputField(Locators.TITLE)
    content = InputField(Locators.CONTENT)
    save_button = Button(Locators.SAVE_BUTTON)
