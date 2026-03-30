"""Tests for API response mocking and network interception."""

import json

import pytest
from playwright.async_api import expect

# API Call from browser
# API call contact server return back response to browser
# browser uses response to show the html output


@pytest.mark.smoke
async def intercept_cart(route):
    """Intercept and mock cart API response.

    Args:
        route: Playwright route object.

    """
    await route.fulfill(json={"message": "No Product in Cart"})


with open("data/credentials.json") as f:
    test_data = json.load(f)
    user_credentials_list = test_data["user_credentials"]


@pytest.mark.smoke
@pytest.mark.asyncio
@pytest.mark.parametrize("user_credentials", user_credentials_list)
async def test_network1(page, user_credentials):
    """Test network interception with mocked API responses.

    Args:
        page: Playwright page fixture.
        user_credentials: Parametrized user credentials.

    """
    await page.goto("https://rahulshettyacademy.com/client")
    await page.route(
        "https://rahulshettyacademy.com/api/ecom/user/get-cart-products/63c993f3568c3e9fb1fcd1c2",
        intercept_cart,
    )
    await page.get_by_placeholder("email@example.com").fill(
        user_credentials["userEmail"]
    )
    await page.get_by_placeholder("enter your passsword").fill(
        user_credentials["userPassword"]
    )
    await page.get_by_role("button", name="Login").click()
    await page.get_by_role("button", name="Cart").click()
    await expect(
        page.get_by_role("heading", name="No Products in Your Cart !")
    ).to_be_visible()
