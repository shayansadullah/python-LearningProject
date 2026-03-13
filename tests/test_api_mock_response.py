from playwright.async_api import expect, async_playwright
import pytest

#API Call from browser
#API call contact server return back response to browser
#browser uses response to show the html output

@pytest.mark.smoke
async def intercept_cart(route):
    await route.fulfill(json={"message": "No Product in Cart"})


@pytest.mark.smoke
@pytest.mark.asyncio
async def test_network1():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto('https://rahulshettyacademy.com/client')
        await page.route('https://rahulshettyacademy.com/api/ecom/user/get-cart-products/63c993f3568c3e9fb1fcd1c2', intercept_cart)
        await page.get_by_placeholder('email@example.com').fill('shayansadullah@gmail.com')
        await page.get_by_placeholder('enter your passsword').fill('abC1983def$')
        await page.get_by_role('button', name='Login').click()
        await page.get_by_role('button', name='Cart').click()
        await expect(page.get_by_role('heading', name='No Products in Your Cart !')).to_be_visible()

