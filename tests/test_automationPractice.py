import asyncio
from playwright.async_api import expect
import pytest

@pytest.mark.smoke
@pytest.mark.asyncio
async def test_UIChecks(page):
    #Hide / Display
    await page.goto("https://rahulshettyacademy.com/AutomationPractice")
    await expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    await page.get_by_role("Button", name="Hide").click()
    await expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    #AlertBoxes:
    page.on("dialog", lambda dialog: dialog.accept())
    await page.get_by_role("Button", name="Confirm").click()
    await asyncio.sleep(5)

@pytest.mark.smoke
@pytest.mark.asyncio
async def test_tableRowCheck(page):
    #Using Tables:
    await page.goto("https://rahulshettyacademy.com/SeleniumPractise/#/offers")

    for index in range(await page.locator("th").count()):
        if await page.locator("th").nth(index).filter(has_text="Price").count() > 0:
            priceCol = index
            print(f"Price column value is {priceCol}")
            break
    riceRow = page.locator("tr").filter(has_text="Rice")
    await expect(riceRow.locator("td").nth(priceCol)).to_have_text("37")


@pytest.mark.smoke
@pytest.mark.asyncio
async def test_hoverOver(page):
    await page.goto('https://rahulshettyacademy.com/AutomationPractice/')
    await page.locator('#mousehover').hover()
    await page.get_by_role("link", name="Top").click()
