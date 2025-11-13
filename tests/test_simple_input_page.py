from pages.simple_input_page import SimpleInputPage



def test_valid_text_input(page):
    expected_text  = 'Expected'
    simple_input_page = SimpleInputPage(page)
    simple_input_page.open()
    simple_input_page.fill_text(expected_text)
    simple_input_page.check_result_text(expected_text)

def test_one_char_input(page):
    simple_input_page = SimpleInputPage(page)
    simple_input_page.open()
    simple_input_page.fill_text('s')
    simple_input_page.check_error_message('Please enter 2 or more characters')