"""Basic Playwright functionality tests including login scenarios."""

import json

import pytest
from playwright.async_api import expect

with open("data/pagePractice.json") as f:
    test_data = json.load(f)
    user_credentials_list = test_data["user_credentials"]


@pytest.mark.smoke
@pytest.mark.asyncio
async def test_thirdCheck(page):
    """Test basic page navigation.

    Args:
        page: Playwright page fixture.

    """
    await page.goto("https://rahulshettyacademy.com")


@pytest.mark.smoke
@pytest.mark.asyncio
@pytest.mark.parametrize("user_credentials", user_credentials_list)
async def test_SuccessfulLogin(page, user_credentials):
    """Test successful login with valid credentials.

    Args:
        page: Playwright page fixture.
        user_credentials: Parametrized user credentials.

    """
    await page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    await page.get_by_label("Username:").fill(user_credentials["userEmail"])
    await page.get_by_label("Password:").fill(user_credentials["userPassword"])
    await page.get_by_role("combobox").select_option("teach")
    await page.get_by_role("checkbox", name="terms").check()
    await page.get_by_role("button", name="Sign In").click()


@pytest.mark.smoke
@pytest.mark.asyncio
async def test_FailedLogin(page):
    """Test failed login with invalid credentials.

    Args:
        page: Playwright page fixture.

    """
    await page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    await page.get_by_label("Username:").fill("rahulshettyacademy")
    await page.get_by_label("Password:").fill("Learning@830$3mK2-abc")
    await page.get_by_role("combobox").select_option("teach")
    await page.get_by_role("checkbox", name="terms").check()
    await page.get_by_role("button", name="Sign In").click()
    await expect(page.get_by_text("Incorrect username/password.")).to_be_visible()


@pytest.mark.smoke
@pytest.mark.asyncio
@pytest.mark.parametrize("user_credentials", user_credentials_list)
async def test_RunFirefox(page, user_credentials):
    """Test login functionality in Firefox browser.

    Args:
        page: Playwright page fixture.
        user_credentials: Parametrized user credentials.

    """
    await page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    await page.get_by_label("Username:").fill(user_credentials["userEmail"])
    await page.get_by_label("Password:").fill(user_credentials["userPassword"])
    await page.get_by_role("combobox").select_option("teach")
    await page.get_by_role("checkbox", name="terms").check()
    await page.get_by_role("button", name="Sign In").click()
