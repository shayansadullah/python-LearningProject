from tkinter import dialog

import time

from playwright.sync_api import Page, expect

def test_UIChecks(page: Page):

    #Hide / Display
    page.goto("https://rahulshettyacademy.com/AutomationPractice")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("Button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    #AlertBoxes:
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("Button", name="Confirm").click()
    time.sleep(5)


def test_tableRowCheck(page: Page):
    #Using Tables:
    page.goto("https://rahulshettyacademy.com/SeleniumPractise/#/offers")

    for index in range(page.locator("th").count()):
        if (page.locator("th").nth(index).filter(has_text="Price")).count() > 0:
            priceCol = index
            print(f"Price column value is {priceCol}")
            break
    riceRow = page.locator("tr").filter(has_text="Rice")
    expect(riceRow.locator("td").nth(priceCol)).to_have_text("37")


def test_hoverOver(page: Page):
    page.goto('https://rahulshettyacademy.com/AutomationPractice/')
    page.locator('#mousehover').hover()
    page.get_by_role("link", name="Top").click()



