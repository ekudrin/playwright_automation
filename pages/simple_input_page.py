from playwright.sync_api import expect

from pages.base_page import BasePage


class SimpleInputPage(BasePage):

    text_input = "input[name='text_string']"
    result_message = "#result-text"
    error_message = "#error_1_id_text_string"


    def open(self):
        self.page.goto(self.HOMEPAGE_URL + "elements/input/simple")


    def fill_text(self, text):
        self.page.fill(self.text_input, text)
        self.page.keyboard.press('Enter')

    def check_result_text(self,expected_text):
        message = self.page.locator(self.result_message)
        expect(message).to_contain_text(expected_text)

    def check_error_message(self,error_text):
        message = self.page.locator(self.error_message)
        expect(message).to_contain_text(error_text)