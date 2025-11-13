from pages.simple_input_page import SimpleInputPage



def test_text_input(page):
    expected_text  = 'Expected'
    simple_input_page = SimpleInputPage(page)
    simple_input_page.open()
    simple_input_page.fill_text(expected_text)
    simple_input_page.check_result_text(expected_text)