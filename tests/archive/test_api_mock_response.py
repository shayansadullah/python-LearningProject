from playwright.sync_api import Page, expect
import pytest


#API Call from browser
#API call contact server return back response to browser
#browser uses response to show the html output

@pytest.mark.skip(reason="test_network1")
def intercept_cart(route):
    route.fulfill(json={"message": "No Product in Cart"})


def test_network1(page: Page):
    page.goto('https://rahulshettyacademy.com/client')

    page.route('https://rahulshettyacademy.com/api/ecom/user/get-cart-products/63c993f3568c3e9fb1fcd1c2', intercept_cart)

    page.get_by_placeholder('email@example.com').fill('shayansadullah@gmail.com')
    page.get_by_placeholder('enter your passsword').fill('abC1983def$')
    page.get_by_role('button', name='Login').click()
    page.get_by_role('button', name='Cart').click()
    expect(page.get_by_role('heading', name='No Products in Your Cart !')).to_be_visible()

