from playwright.async_api import async_playwright, expect
import pytest
import json

with open("src/data/pagePractice.json") as f:
    test_data = json.load(f)
    user_credentials_list = test_data['user_credentials']


@pytest.mark.smoke
@pytest.mark.asyncio
async def test_thirdCheck():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://rahulshettyacademy.com")

@pytest.mark.smoke
@pytest.mark.asyncio
@pytest.mark.parametrize('user_credentials', user_credentials_list)
async def test_SuccessfulLogin(user_credentials):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://rahulshettyacademy.com/loginpagePractise/")
        await page.get_by_label('Username:').fill(user_credentials['userEmail'])
        await page.get_by_label('Password:').fill(user_credentials['userPassword'])
        await page.get_by_role('combobox').select_option('teach')
        await page.get_by_role('checkbox', name='terms').check()
        await page.get_by_role('button', name='Sign In').click()


@pytest.mark.smoke
@pytest.mark.asyncio
async def test_FailedLogin():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://rahulshettyacademy.com/loginpagePractise/")
        await page.get_by_label('Username:').fill('rahulshettyacademy')
        await page.get_by_label('Password:').fill('Learning@830$3mK2-abc')
        await page.get_by_role('combobox').select_option('teach')
        await page.get_by_role('checkbox', name='terms').check()
        await page.get_by_role('button', name='Sign In').click()
        await expect(page.get_by_text('Incorrect username/password.')).to_be_visible()

@pytest.mark.smoke
@pytest.mark.asyncio
@pytest.mark.parametrize('user_credentials', user_credentials_list)
async def test_RunFirefox(user_credentials):
    async with async_playwright() as playwright:
        browser = await playwright.firefox.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("https://rahulshettyacademy.com/loginpagePractise/")
        await page.get_by_label('Username:').fill(user_credentials['userEmail'])
        await page.get_by_label('Password:').fill(user_credentials['userPassword'])
        await page.get_by_role('combobox').select_option('teach')
        await page.get_by_role('checkbox', name='terms').check()
        await page.get_by_role('button', name='Sign In').click()
