import time
import pytest
from playwright.async_api import async_playwright, expect
from src.utils.apiBase import APIUtils

@pytest.mark.skip(reason="test_e2e_web_api is an end-to-end test that requires a live server and may not be suitable for regular test runs.")
@pytest.mark.asyncio
async def test_e2e_web_api():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        api_utils = APIUtils()
        order_response = await api_utils.createOrder(playwright)
        message = order_response['message']
        token = order_response['token']
        assert message == 'Product Added To Cart', f"Expected 'Product Added To Cart' but got '{message}'"

        orderId = await api_utils.getOrderId()

        print(f"Here is the response body for the order: {message}")

        # Inject token into browser to share the same session
        await page.goto('https://rahulshettyacademy.com/client')
        await page.evaluate(f"window.localStorage.setItem('token', '{token}')")
        await page.reload()

        await page.get_by_role('button', name='Cart').click()

        foo = page.locator('.itemNumber').filter(has_text=orderId)
        expect(foo).to_be_visible()
