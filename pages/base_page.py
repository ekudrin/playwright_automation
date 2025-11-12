class BasePage:

    HOMEPAGE_URL = 'https://www.qa-practice.com/'

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(self.HOMEPAGE_URL)

