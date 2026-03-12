from src.pageObjects.CartPage import CartPage

class DashboardPage:
    def __init__(self, page):
        self.page = page

    async def add_to_cart(self, product_name):
        await self.page.locator(".col-lg-4").filter(has_text=product_name).get_by_role("button", name="Add To Cart").click()
        cartPage = CartPage(self.page)
        return cartPage
