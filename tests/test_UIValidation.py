import time

from playwright.sync_api import Page, expect

def test_UIValidation(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label('Username:').fill('rahulshettyacademy')
    page.get_by_label('Password:').fill('Learning@830$3mK2')
    page.get_by_role('combobox').select_option('teach')
    page.get_by_role('checkbox', name='terms').check()
    page.get_by_role('button', name='Sign In').click()
    iphoneProduct = page.locator('app-card').filter(has_text='iphone X')
    iphoneProduct.get_by_role('button').click()
    nokiaProduct = page.locator('app-card').filter(has_text='Nokia Edge')
    nokiaProduct.get_by_role('button').click()
    page.get_by_text('Checkout').click()
    expect(page.locator('.media-body')).to_have_count(2)
    time.sleep(5)


def test_childWindowHandle(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as newPage_info:
        page.locator(".blinkingText")[0].click()
        childpage = newPage_info.value
        text = childpage.locator(".red").text_content()
        print(text)
