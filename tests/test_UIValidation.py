import asyncio
import json

from playwright.async_api import expect
import pytest

with open("src/data/pagePractice.json") as f:
    test_data = json.load(f)
    user_credentials_list = test_data['user_credentials']


@pytest.mark.smoke
@pytest.mark.asyncio
@pytest.mark.parametrize('user_credentials', user_credentials_list)
async def test_UIValidation(page, user_credentials):
    await page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    await page.get_by_label('Username:').fill(user_credentials['userEmail'])
    await page.get_by_label('Password:').fill(user_credentials['userPassword'])
    await page.get_by_role('combobox').select_option('teach')
    await page.get_by_role('checkbox', name='terms').check()
    await page.get_by_role('button', name='Sign In').click()
    iphoneProduct = page.locator('app-card').filter(has_text='iphone X')
    await iphoneProduct.get_by_role('button').click()
    nokiaProduct = page.locator('app-card').filter(has_text='Nokia Edge')
    await nokiaProduct.get_by_role('button').click()
    await page.get_by_text('Checkout').click()
    await expect(page.locator('.media-body')).to_have_count(2)
    await asyncio.sleep(5)


@pytest.mark.smoke
@pytest.mark.asyncio
async def test_childWindowHandle(page):
    await page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    async with page.expect_popup() as newPage_info:
        await page.locator(".blinkingText").first.click()

    childpage = await newPage_info.value
    text = await childpage.locator(".red").text_content()
    print(text)
