from playwright.sync_api import Page, Playwright, expect

def test_thirdCheck(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")

def test_SuccessfulLogin(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label('Username:').fill('rahulshettyacademy')
    page.get_by_label('Password:').fill('Learning@830$3mK2')
    page.get_by_role('combobox').select_option('teach')
    page.get_by_role('checkbox', name='terms').check()
    page.get_by_role('button', name='Sign In').click()

def test_FailedLogin(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label('Username:').fill('rahulshettyacademy')
    page.get_by_label('Password:').fill('Learning@830$3mK2-abc')
    page.get_by_role('combobox').select_option('teach')
    page.get_by_role('checkbox', name='terms').check()
    page.get_by_role('button', name='Sign In').click()
    expect(page.get_by_text('Incorrect username/password.')).to_be_visible()

def test_RunFirefox(playwright: Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label('Username:').fill('rahulshettyacademy')
    page.get_by_label('Password:').fill('Learning@830$3mK2')
    page.get_by_role('combobox').select_option('teach')
    page.get_by_role('checkbox', name='terms').check()
    page.get_by_role('button', name='Sign In').click()
