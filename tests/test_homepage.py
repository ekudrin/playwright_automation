from playwright.sync_api import Page, expect


HOMEPAGE_URL  = 'https://www.qa-practice.com/'


def test_homepage(page: Page):
    page.goto(HOMEPAGE_URL)
    page.get_by_role('link', name='Text input').click()
    expect(page.get_by_text('Text string*')).to_be_visible()
