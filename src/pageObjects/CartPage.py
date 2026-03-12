class CartPage:
    def __init__(self, page):
        self.page = page

    async def navigate(self):
        await self.page.goto("https://rahulshettyacademy.com/client/#/dashboard/cart")

    async def get_cart_item(self, product_name):
        return await self.page.locator("li.items").filter(has_text=product_name).text_content()

