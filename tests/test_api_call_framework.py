import json

import pytest
from playwright.async_api import async_playwright, expect

from src.pageObjects.LoginPage import LoginPage
from src.utils.apiBase import APIUtils

with open("src/data/credentials.json") as f:
    test_data = json.load(f)
    user_credentials_list = test_data["user_credentials"]


@pytest.mark.smoke
@pytest.mark.asyncio
@pytest.mark.parametrize("user_credentials", user_credentials_list)
async def test_e2e_web_api(user_credentials):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        api_utils = APIUtils()
        order_response = await api_utils.createOrder(playwright, user_credentials)
        message = order_response["message"]
        token = order_response["token"]
        assert message == "Product Added To Cart", (
            f"Expected 'Product Added To Cart' but got '{message}'"
        )

        orderId = await api_utils.getOrderId()

        print(f"Here is the response body for the order: {message}")

        # Inject token into browser to share the same session
        loginPage = LoginPage(page)
        await loginPage.navigate()

        await page.evaluate(f"window.localStorage.setItem('token', '{token}')")
        await page.reload()

        await page.get_by_role("button", name="Cart").click()

        orderInfo = page.locator(".itemNumber").filter(has_text=orderId)
        await expect(orderInfo).to_be_visible()
